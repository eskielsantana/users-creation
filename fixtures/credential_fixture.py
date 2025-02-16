import requests

from fixtures.api_fixture import ApiFixture


class CredentialFixture(ApiFixture):
    endpoint = 'auth/user_info'

    def __init__(self):
        super().__init__(self.endpoint)

    def check_if_credential_is_valid(self):
        response = requests.get(self.request_url, headers=self.headers)

        if response.status_code == 403:
            raise Exception(f"Authentication code is invalid! Please refresh it!")

        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}")