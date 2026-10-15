import requests
import pytest
import random

from urls import LOGIN, REGISTER, CREATE_LISTING
from data import CATEGORY_LIST, CITY_LIST, CONDITION_LIST
from helpers import generate_email, generate_password, generate_name, generate_text, generate_number


@pytest.fixture
def generate_user():
    return {
        "email": generate_email(),
        "password": generate_password(),
    }


@pytest.fixture
def generate_listing():
    payload = {
        'name': generate_name(),
        'category': random.choice(CATEGORY_LIST),
        'condition': random.choice(CONDITION_LIST),
        'city': random.choice(CITY_LIST),
        'description': generate_text(),
        'price': generate_number(),
    }
    files = {
        key: (None, str(value))
        for key, value in payload.items()
    }
    return files


@pytest.fixture
def registred_user(generate_user):
    payload = generate_user
    payload['submitPassword'] = payload['password']
    response = requests.post(REGISTER, data=payload)
    return payload, response


@pytest.fixture
def logged_user(registred_user):
    payload = registred_user[0]
    response = requests.post(LOGIN, data=payload)
    token = response.json()['token']['access_token']
    return response, token


@pytest.fixture
def second_logged_user():
    payload = {
        "email": generate_email(),
        "password": generate_password(),
    }
    payload['submitPassword'] = payload['password']
    requests.post(REGISTER, data=payload)
    response = requests.post(LOGIN, data=payload)
    token = response.json()['token']['access_token']
    return token


@pytest.fixture
def create_listing(generate_listing, logged_user):
    payload = generate_listing
    token = logged_user[1]
    response = requests.post(
        CREATE_LISTING,
        headers={"Authorization": f"Bearer {token}"},
        files=payload
    )
    id = response.json()['id']
    return response, id

