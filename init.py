import argparse

from dotenv import load_dotenv

from fixtures.credential_fixture import CredentialFixture
from fixtures.permission_fixture import PermissionFixture
from services.random_user_service import RandomUserService
from services.user_service import UserService


def load_environment():
    parser = argparse.ArgumentParser(description='Run the UsersCreation script with a specified environment.')
    parser.add_argument('--env', type=str, default='dev', help='The environment to use (e.g., dev, prod)')
    args = parser.parse_args()

    env_file = f"{args.env}.env"
    load_dotenv(env_file)


class Main:
    def __init__(self):
        load_environment()
        self.credential_fixture = CredentialFixture()
        self.permission_fixture = PermissionFixture()
        self.user_service = UserService()
        self.random_user_service = RandomUserService()
        self.credential_fixture.check_if_credential_is_valid()

        self.test_random_user_creation()
        # self.test_permission_fixture()
        # self.test_setting_fixture()

    def test_permission_fixture(self):
        all_perms = self.permission_fixture.find_all(1, 20)

        TEST_USER_WITH_NO_FINANCIAL_PERMS = [self.perm_enabled('Core'), self.perm_enabled('Wbs')]

        self.user_service.process_user(
            {'first_name': 'Eze', 'last_name': 'Test3', 'email': 'eze.test3@automation.com'},
            TEST_USER_WITH_NO_FINANCIAL_PERMS,
            all_perms)

    def test_setting_fixture(self):
        user_id = 118
        self.user_service.setting_fixture.set(user_id, 'SHOW_GRID_LAYOUT_UPDATES', True)

    def test_random_user_creation(self):
        a = self.random_user_service.create()

        print(a)

    @staticmethod
    def perm_enabled(name):
        return {'name': name, 'types': ['Enabled']}


if __name__ == "__main__":
    Main()
