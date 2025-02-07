from terminaltables import AsciiTable
from pprint import pprint
from headhunter_job_seecker import get_hh_statistic
from superjob_job_seecker import get_sj_statistic


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
    languages = ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'C']

    sj_vacancies_statistic = get_sj_statistic(languages)
    hh_vacancies_statistic = get_hh_statistic(languages)

    print(make_table(hh_vacancies_statistic, languages, title='HeadHunter'))
    print(make_table(sj_vacancies_statistic, languages, title='SuperJob'))

if __name__ == "__main__":
    main()