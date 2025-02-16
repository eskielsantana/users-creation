import requests
import json
from fixtures.api_fixture import ApiFixture


def role_request_object(role_id, permission_id):
    return {
        'auth_instance_id': role_id,
        'has_permission': True,
        'permission_id': permission_id
    }


class RoleFixture(ApiFixture):
    endpoint = 'api/v1/roles/'

    def __init__(self):
        super().__init__(self.endpoint)

    def create(self, user_name):
        body = {
            'name': f"{user_name} DONT CHANGE!",
            'description': 'This role has been created for automation tests and must not be changed or deleted!'
        }

        response = requests.post(self.request_url, headers=self.headers, data=json.dumps(body))

        if response.status_code != 201:
            raise Exception(f"Request failed with status code {response.status_code}")

        return response.json()
