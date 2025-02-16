import json

import requests

from fixtures.api_fixture import ApiFixture


def setting_request_object(setting_name, user_id, value):
    return {
        'name': setting_name,
        'user': user_id,
        'value': 'True' if value else 'False'
    }


class SettingFixture(ApiFixture):
    endpoint = 'api/v1/global_settings/'

    def __init__(self):
        super().__init__(self.endpoint)

    def get_user_settings(self, user_id):
        url = f"{self.request_url}?filter_expression=user eq {user_id}"

        response = super().get(url)
        results = response.get('results', [])

        return results

    def user_has_setting(self, user_id, setting):
        all_settings = self.get_user_settings(user_id)

        for user_setting in all_settings:
            if user_setting.get('name') == setting:
                return user_setting
        return {}

    def set(self, user_id, setting_name, value=True):
        setting = self.user_has_setting(user_id, setting_name)
        if setting:
            if setting.get('value') != value:
                body = setting_request_object(setting_name, user_id, value)
                response = super().put(setting.get('id'), json.dumps(body))
            else:
                print(f"Setting {setting.get('name')} already has value {setting.get('value')}")
                return {}
        else:
            body = setting_request_object(setting_name, user_id, value)
            response = super().post(self.request_url, json.dumps(body))

        return response
