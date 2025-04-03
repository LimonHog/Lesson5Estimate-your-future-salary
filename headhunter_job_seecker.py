import requests
from itertools import count
from salary_perdicter import predict_rub_salary

    

def get_hh_statistic(languages):
    region_id = '1'
    per_page = 100
    hh_vacancies_statistic = {}
    for language in languages:
        counter = 0
        for page in count(0, 1):
            
            url = "https://api.hh.ru/vacancies"
            params= {
                'text' : language,
                'area' : region_id,
                'page' : page,
                'per_page': per_page
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
            try:  
                average_salary = sum(salaries)/counter
            except ZeroDivisionError:
                print("U can't didvide by zero")
                average_salary = 0
                
            average_salary = int(average_salary)   

        hh_vacancies_statistic[language] = {
            "vacancies_found": response['found'],
            "vacancies_processed": counter,
            "average_salary": average_salary
        }
    return hh_vacancies_statistic
