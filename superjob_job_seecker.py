import requests
from itertools import count
from salary_perdicter import predict_rub_salary




def get_sj_statistic(languages, api):
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
                'X-Api-App-Id': api
            }

            superjob_url = f'https://api.superjob.ru/2.0/vacancies/'

            sj_response = requests.get(superjob_url, headers=headers, params=params)
            sj_response.raise_for_status()
            sj_response = sj_response.json()

            salaries = []
            
            for one_job_lure in sj_response['objects']:
                if one_job_lure['currency'] == 'rub': 
                    if not one_job_lure['payment_from'] or not one_job_lure['payment_to']:
                        continue
                    counter += 1
                     
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