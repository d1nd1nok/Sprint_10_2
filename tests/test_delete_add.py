import requests

from urls import DELETE_LISTING


class TestDeleteAdd():
    def test_success_delete_add(self, create_listing, logged_user):
        response, listing_id = create_listing
        token = logged_user[1]

        response = requests.delete(
            f"{DELETE_LISTING}{listing_id}",
            headers={'Authorization': f'Bearer {token}'}
        )
        assert response.status_code == 200
