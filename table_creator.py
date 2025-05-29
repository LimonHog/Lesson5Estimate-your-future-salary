from terminaltables import AsciiTable
from headhunter_job_seecker import get_hh_statistic
from superjob_job_seecker import get_sj_statistic
from dotenv import load_dotenv
import os


def make_table(vacancies_statistic, languages, title):
    
    js_vacancies_table = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    
    for language in languages:
        js_vacancies_table.append([language, vacancies_statistic[language]['vacancies_found'], vacancies_statistic[language]['vacancies_processed'], vacancies_statistic[language]['average_salary']])
        
    sj_table = AsciiTable(js_vacancies_table)
    sj_table.title = f'{title} Moscow'
    return sj_table.table


def main():
    load_dotenv() 

    languages = ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'C']
    super_job_key = os.environ['API_SUPERJOB']

    sj_vacancies_statistic = get_sj_statistic(languages, super_job_key)
    hh_vacancies_statistic = get_hh_statistic(languages)

    print(make_table(hh_vacancies_statistic, languages, title='HeadHunter'))
    print(make_table(sj_vacancies_statistic, languages, title='SuperJob'))

if __name__ == "__main__":
    main()