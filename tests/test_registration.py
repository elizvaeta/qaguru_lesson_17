import requests
from tests.conftest import BASE_URL


def test_registration():
    url = '/api/register'

    body = {
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    }

    response = requests.post(url=BASE_URL + url, json=body)

    response_body = response.json()

    assert response.status_code == 200
    assert 'id' in response_body
    assert 'token' in response_body


def test_registration_negative_empty_password():
    url = '/api/register'

    body = {
        'email': 'eve.holt@reqres.in',
        'password': ''
    }

    response = requests.post(url=BASE_URL + url, json=body)

    response_body = response.json()

    expected_body = {
        'error': 'Missing password'
    }

    assert response.status_code == 400
    assert response_body == expected_body
