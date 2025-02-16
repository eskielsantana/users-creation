import json

import requests

from fixtures.api_fixture import ApiFixture


class PermissionFixture(ApiFixture):
    endpoint = 'api/v1/permissions_tree_view_compacted/role/module/'

    def __init__(self):
        super().__init__(self.endpoint)

    def find_all(self, segment, region):
        url = f"{self.request_url}?segment={segment}&regions={region}"

        response = super().get(url)

        return response.json()

    def submit(self, body):
        response = requests.post(self.request_url, headers=self.headers, data=json.dumps(body))

        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}")

        return response
