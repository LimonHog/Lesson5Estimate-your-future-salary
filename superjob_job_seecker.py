import requests
from itertools import count
from dotenv import load_dotenv
import os
from salary_perdicter import predict_rub_salary




def get_sj_statistic(languages):
    load_dotenv()
    vacancies_statistic = {}
    for language in languages:
        counter = 0
        for page in count(0, 1): 
            
            params = {
                'town': 'Москва',
                'keyword': language,
                'page': page,
                'count': 100
            }
            headers = {
                'X-Api-App-Id': os.environ['API_SUPERJOB']
            }

            superjob_url = f'https://api.superjob.ru/2.0/vacancies/'

            sj_response = requests.get(superjob_url, headers=headers, params=params)
            sj_response.raise_for_status()
            sj_response = sj_response.json()

            salaries = []
            
            for one_job_lure in sj_response['objects']:
                if one_job_lure['currency'] == 'rub': 
                    if one_job_lure['payment_from'] or one_job_lure['payment_to']:
                        counter += 1
                        
                        sj_salary = predict_rub_salary(one_job_lure['payment_from'], one_job_lure['payment_to'])  
                        salaries.append(int(predict_rub_salary(one_job_lure['payment_from'], one_job_lure['payment_to']))) 

            try:
                average_salary = sum(salaries)/counter   
            except ZeroDivisionError:
                average_salary = 0    

            vacancies_statistic[language] = {
                "vacancies_found": sj_response['total'],
                "vacancies_processed": counter,
                "average_salary": average_salary
            }

            if not sj_response['more']:
                break
    return vacancies_statistic