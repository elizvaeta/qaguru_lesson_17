import requests
from helpers.json_validator import assert_json_schema
from tests.conftest import BASE_URL


def test_post_user():
    url = '/api/users'

    name = 'morpheus'
    job = 'leader'

    body = {
        'name': name,
        'job': job,
    }

    response = requests.post(url=BASE_URL + url, json=body)

    response_body = response.json()

    assert response.status_code == 201
    assert response_body['name'] == name
    assert response_body['job'] == job

    assert_json_schema(response=response, schema_name='post_user.json')
