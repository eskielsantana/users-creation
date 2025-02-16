import json

from fixtures.api_fixture import ApiFixture


class PermissionFixture(ApiFixture):
    endpoint = 'api/v1/permissions_tree_view_compacted/role/module/'

    def __init__(self):
        super().__init__(self.endpoint)

    def find_all(self, segment, region):
        url = f"{self.request_url}?segment={segment}&regions={region}"

        response = super().get(url)

        return response

    def submit(self, body):
        response = super().post(self.request_url, json.dumps(body))

        return response
