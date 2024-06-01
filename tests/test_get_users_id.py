import requests
from helpers.json_validator import assert_json_schema
from tests.conftest import BASE_URL


def test_get_user():
    user_id = 2
    url = f'/api/users/{user_id}'

    response = requests.get(url=BASE_URL + url)

    response_body = response.json()

    assert response.status_code == 200
    assert 'data' in response_body

    assert_json_schema(response=response, schema_name='get_user.json')


def test_negative_random_id():
    user_id = 999999999
    url = f'/api/users/{user_id}'

    response = requests.get(url=BASE_URL + url)

    response_body = response.json()

    assert response.status_code == 404
    assert not response_body
