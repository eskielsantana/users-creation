import argparse

from dotenv import load_dotenv

from fixtures.credential_fixture import CredentialFixture
from fixtures.permission_fixture import PermissionFixture
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
        self.credential_fixture.check_if_credential_is_valid()

        self.test_permission_fixture()

    def test_permission_fixture(self):
        all_perms = self.permission_fixture.find_all(1, 20)

        TEST_USER_WITH_NO_FINANCIAL_PERMS = [self.perm_enabled('Core'), self.perm_enabled('Wbs')]

        self.user_service.process_user(
            {'first_name': 'Eze', 'last_name': 'Test3', 'email': 'eze.test3@automation.com'},
            TEST_USER_WITH_NO_FINANCIAL_PERMS,
            all_perms)

    @staticmethod
    def perm_enabled(name):
        return {'name': name, 'types': ['Enabled']}


if __name__ == "__main__":
    Main()
