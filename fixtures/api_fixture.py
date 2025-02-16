import os

import requests


class ApiFixture:

    def __init__(self, endpoint):
        web_url = os.getenv('WEB_URL')
        authorization = os.getenv('AUTH')

        self.request_url = f"{web_url}{endpoint}"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': authorization,
        }


    def get(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        if response.status_code != 201:
            raise Exception(f"Request failed with status code {response.status_code}")

        return response.json()


    def post(self, url, body):
        response = requests.post(url, headers=self.headers, data=body)
        response.raise_for_status()
        return response.json()
