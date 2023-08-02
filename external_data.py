""""Импорт тестовых данных"""
import requests


def load_external_data():
    """"Загрузка тестовых данных с внешнего источника"""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Ошибка загрузки с сайта {url}. Статус код: {response.status_code}")