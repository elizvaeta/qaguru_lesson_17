import requests
from helpers.json_validator import assert_json_schema
from tests.conftest import BASE_URL


def test_put_user(user):
    user_id = user['id']
    url = f'/api/users/{user_id}'

    name = 'updated name'

    body = {
        'name': name,
    }

    response = requests.put(url=BASE_URL + url, json=body)

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['name'] == name
    assert 'job' not in response_body

    assert_json_schema(response=response, schema_name='put_user.json')
