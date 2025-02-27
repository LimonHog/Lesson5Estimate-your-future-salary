import requests
from pprint import pprint
from itertools import count


def predict_rub_salary(salary): 
    if salary['from'] and salary['to']:
        return (salary['from'] + salary['to'])/2
    if salary['from'] == None:
        return salary['to']*0.8
    if salary['to'] == None:
        return salary['from']*1.2

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
            for item in response['items']:
                if item['salary'] and item['salary']['currency'] == 'RUR':
                    counter += 1
                    salaries.append(int(predict_rub_salary(item['salary'])))    
            average_salary = sum(salaries)/counter
            average_salary = int(average_salary)   

        hh_vacancies_statistic[language] = {
            "vacancies_found": response['found'],
            "vacancies_processed": counter,
            "average_salary": average_salary
        }
    return hh_vacancies_statistic
