import json

import requests

from fixtures.api_fixture import ApiFixture


class UserFixture(ApiFixture):
    endpoint = 'api/v1/users/'

    def __init__(self):
        super().__init__(self.endpoint)

    def create(self, email, first_name, last_name, role_id):
        body = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password': 'fresnel123',
            'roles': [role_id]
        }

        response = requests.post(self.request_url, headers=self.headers, data=json.dumps(body))

        if response.status_code != 201:
            raise Exception(f"Request failed with status code {response.status_code}")

        return response.json()

    def user_exists(self, email):
        url = f"{self.request_url}?full_name_with_email=${email}"

        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        if len(response.json().get('results', [])) > 0:
            return True
        return False
