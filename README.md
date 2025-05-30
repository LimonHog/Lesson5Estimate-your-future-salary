# Расчёт будущей зарпаты

Данный проект может рассчитывать среднюю заработную плату(дальше зп), основываясь на данных с сайтов [SuperJob](https://www.superjob.ru) и [HeadHunter](https://hh.ru). Среднюю зп, количество найденных и проанализированных вакансий код выводит таблицей. Уточню, что проект рассчитывает средние зарплаты по вакансиям в Москве, однако это можно изменить.

# Как установить

Прежде чем запускать код необходимо установить некоторые библиотеки. Их всех с нужными версиями можно найти в файле `requirements.txt`, а для установки используйте команду:
```
pip install -r requirements.txt
```

Чтобы код выполнял свою работу необходимо написать команду:
```
python table_creator.py
```

Нельзя не упомянуть и то, что для работы вам необходимо иметь свой SuperJob API токен. Он хранятся в `.env` файле в следущем виде:
```
API_SUPERJOB='ваш токен'
```

Позже он передаётся в переменную `super_job_api` внутри файла `table_creator.py`:
```
super_job_api = os.environ['API_SUPERJOB']
```
Далее эта переменная перердаётся в качестве аргумента функции
 ```
get_sj_statistic(languages, super_job_api)
```
После она передаётся в headers внутри самой функции(код функции находится в файле `superjob_job_seecker.py`):
```
headers = {
    'X-Api-App-Id': api
}
```

# Как работает код?

При запуске сначала за работу принимаются файлы `superjob_job_seecker.py` и `headhunter_job_seecker.py`, в них происходит сбор и анализ информации. Ещё в коде файла `salary_predicter.py` хранится функция для расчёта зп. А после вся эта информация передаётся в основной `table_creator.py` файл. Там она уже и преобразуется в удобную для восприятия таблицу.


# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).