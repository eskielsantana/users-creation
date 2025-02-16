import json

from fixtures.api_fixture import ApiFixture


class UserFixture(ApiFixture):
    endpoint = 'api/v1/users/'

    def __init__(self):
        super().__init__(self.endpoint)

    def create(self, email, first_name, last_name, password, role_id):
        body = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password': password,
            'roles': [role_id]
        }

        response = super().post(self.request_url, json.dumps(body))

        return response

    def user_exists(self, email):
        url = f"{self.request_url}?full_name_with_email=${email}"

        response = super().get(url)

        if len(response.get('results', [])) > 0:
            return True
        return False
