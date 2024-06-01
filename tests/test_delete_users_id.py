import requests
from tests.conftest import BASE_URL


def test_delete_user(user):
    user_id = user['id']
    url = f'/api/users/{user_id}'

    response = requests.delete(url=BASE_URL + url)

    response_body = response.text

    assert response.status_code == 204
    assert not response_body
