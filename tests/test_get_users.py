import requests
from helpers.json_validator import assert_json_schema
from tests.conftest import BASE_URL


def test_get_users():
    url = '/api/users'

    response = requests.get(url=BASE_URL + url)

    response_body = response.json()

    assert response.status_code == 200
    assert 'data' in response_body

    assert_json_schema(response=response, schema_name='users.json')


def test_get_users_pagination():
    url = '/api/users'

    page = 3
    per_page = 5

    params = {
        'page': page,
        'per_page': per_page,
    }

    response = requests.get(url=BASE_URL + url, params=params)

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['page'] == page
    assert response_body['per_page'] == per_page
