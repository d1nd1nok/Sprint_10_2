import requests

from urls import LOGIN


class TestLogin():
    def test_login_success(self, registred_user):
        payload = registred_user[0]
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 201
