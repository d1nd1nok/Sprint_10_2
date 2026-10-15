import requests

from urls import REGISTER


class TestRegister():
    def test_success_register(self, generate_user):
        payload = generate_user
        payload['submitPassword'] = payload['password']
        response = requests.post(REGISTER, data=payload)
        assert response.status_code == 201

    def test_reregistration_fail(self, registred_user):
        payload = registred_user[0]
        payload['submitPassword'] = payload['password']
        response = requests.post(REGISTER, data=payload)
        assert response.status_code == 400
