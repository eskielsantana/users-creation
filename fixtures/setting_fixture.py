import requests
import json
from fixtures.api_fixture import ApiFixture


def role_request_object(role_id, permission_id):
    return {
        'auth_instance_id': role_id,
        'has_permission': True,
        'permission_id': permission_id
    }


class SettingFixture(ApiFixture):
    endpoint = 'api/v1/roles/'

    def __init__(self):
        super().__init__(self.endpoint)

    def get_user_settings(self, user_id):
        url = f"{self.request_url}?segment={segment}&regions={region}"

        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}")

        return response.json()

    def user_has_setting(self, user_id, setting):
        all_setings = self.get_user_settings(user_id)

    def set(self, user_name, setting, value=True):
        body = {
            'name': f"{user_name} DONT CHANGE!",
            'description': 'This role has been created for automation tests and must not be changed or deleted!'
        }

        response = requests.post(self.request_url, headers=self.headers, data=json.dumps(body))

        if response.status_code != 201:
            raise Exception(f"Request failed with status code {response.status_code}")

        return response.json()
