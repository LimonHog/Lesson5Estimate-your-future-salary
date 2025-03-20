import requests
from itertools import count
from salary_perdicter import predict_rub_salary

    

def get_hh_statistic(languages):

    hh_vacancies_statistic = {}
    for language in languages:
        counter = 0
        for page in count(0, 1):
            
            url = "https://api.hh.ru/vacancies"
            params= {
                'text' : language,
                'area' : '1',
                'page' : page,
                'per_page': 100
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            response = response.json()
            
            if page >= response['pages']-1:
                break
            salaries = []
            
            for one_job in response['items']:
                if one_job['salary'] and one_job['salary']['currency'] == 'RUR':
                    counter += 1
                    salaries.append(int(predict_rub_salary(one_job['salary']['from'], one_job['salary']['to'])))    
            average_salary = sum(salaries)/counter
            average_salary = int(average_salary)   

        hh_vacancies_statistic[language] = {
            "vacancies_found": response['found'],
            "vacancies_processed": counter,
            "average_salary": average_salary
        }
    return hh_vacancies_statistic
