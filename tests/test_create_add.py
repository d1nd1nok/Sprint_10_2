import requests

from urls import CREATE_LISTING


class TestCreateAdd():
    def test_success_create_add(self, generate_listing, logged_user):
        token = logged_user[1]
        response = requests.post(
            CREATE_LISTING,
            headers={"Authorization": f"Bearer {token}"},
            files=generate_listing
        )
        assert response.status_code == 201
