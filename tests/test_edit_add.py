import pytest
import requests
import random

from urls import UPDATE_LISTING
from data import CHOICE_FIELDS


class TestEditAdd():
    @pytest.mark.parametrize('field', ['name', 'description', 'price'])
    def test_edit_text_field_success(self, field, create_listing, logged_user):
        response, listing_id = create_listing
        token = logged_user[1]
        payload = response.json()
        payload[field] = str(payload[field]) + "1"

        response = requests.patch(
            f"{UPDATE_LISTING}{listing_id}",
            headers={'Authorization': f'Bearer {token}'},
            files={key: (None, str(value)) for key, value in payload.items()}
        )
        assert response.status_code == 200

    @pytest.mark.parametrize('field', ['category', 'condition', 'city'])
    def test_edit_choice_field_success(self, field, create_listing, logged_user):
        response, listing_id = create_listing
        token = logged_user[1]
        payload = response.json()
        current = payload[field]
        options = [v for v in CHOICE_FIELDS[field] if v != current]
        payload[field] = random.choice(options)

        response = requests.patch(
            f"{UPDATE_LISTING}{listing_id}",
            headers={'Authorization': f'Bearer {token}'},
            files={key: (None, str(value)) for key, value in payload.items()}
        )
        assert response.status_code == 200

    def test_edit_not_users_add(self, create_listing, second_logged_user):
        response, listing_id = create_listing
        token = second_logged_user
        payload = response.json()
        payload['name'] = payload['name'] + "1"

        response = requests.patch(
            f"{UPDATE_LISTING}{listing_id}",
            headers={'Authorization': f'Bearer {token}'},
            files={key: (None, str(value)) for key, value in payload.items()}
        )
        assert response.status_code == 401
