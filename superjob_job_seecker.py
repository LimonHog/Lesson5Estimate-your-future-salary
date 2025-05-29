import requests
from itertools import count
from salary_perdicter import predict_rub_salary




def get_sj_statistic(languages, secret_key):
    vacancies_statistic = {}
    for language in languages:
        jobs_counter = 0
        for page in count(0, 1): 
            
            params = {
                'town': 'Москва',
                'keyword': language,
                'page': page,
                'count': 100
            }
            headers = {
                'X-Api-App-Id': secret_key
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
                    job_counter += 1
                     
                    salaries.append(int(predict_rub_salary(one_job_lure['payment_from'], one_job_lure['payment_to'])))

            if not sj_response['more']:
                break
        try:
            average_salary = sum(salaries)/job_counter   
        except ZeroDivisionError:
            average_salary = 0    

        vacancies_statistic[language] = {
            "vacancies_found": sj_response['total'],
            "vacancies_processed": job_counter,
            "average_salary": average_salary
        }      
    return vacancies_statistic