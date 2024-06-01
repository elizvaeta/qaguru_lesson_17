import pytest
import requests
from faker import Faker

BASE_URL = 'https://reqres.in'


# Сделаем вид, что сервис сохраняет наших пользователей,
# и будем использовать новосозданного
@pytest.fixture(scope='function')
def user():
    url = '/api/users'

    name = Faker().name()
    job = Faker().job()

    body = {
        'name': name,
        'job': job,
    }

    response = requests.post(url=BASE_URL + url, json=body)

    return response.json()
