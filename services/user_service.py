from fixtures.credential_fixture import CredentialFixture
from fixtures.permission_fixture import PermissionFixture
from fixtures.role_fixture import RoleFixture, role_request_object
from fixtures.user_fixture import UserFixture


class UserService:
    def __init__(self):
        self.user_fixture = UserFixture()
        self.credential_fixture = CredentialFixture()
        self.permission_fixture = PermissionFixture()
        self.role_fixture = RoleFixture()
        self.user_fixture = UserFixture()

    def find_permission(self, permission_name, permission_type, permissions):
        for permission in permissions:
            if permission['name'] == permission_name:
                if len(permission_type) == 0:
                    return permission['permission_id']
                if 'items' in permission:
                    next_permission_type = permission_type.pop(0)
                    return self.find_permission(next_permission_type, permission_type, permission['items'])
        return None

    def find_layer_permission_id(self, name, perm_type, data):
        permission_type = perm_type.split('.')
        print(permission_type)
        permission_id = self.find_permission(name, permission_type, data['results'])

        if permission_id is None:
            raise Exception(f"Permission or Permission Type not found! ({name}.{type})")
        return permission_id

    def process_user(self, user, permissions, perms_list, c_or_r=False):
        try:
            # if self.user_fixture.user_exists(user):
            #     print(f"A user with the email {user['email']} already exists so this user was skipped!")
            #     return
            #
            # # Create the ROLE
            # role = self.role_fixture.create(f"{user['first_name']} {user['last_name']}")
            # if role is None:
            #     raise Exception("Role wasn't created properly!")
            #
            # # Create the USER
            # new_user = self.user_fixture.create(user['email'], user['first_name'], user['last_name'], role['id'])
            # if new_user is None:
            #     raise Exception("User wasn't created properly!")

            role = {
                'id': 118
            }

            # Assemble a list of permissions to be assigned
            perms_to_link = []
            for permission in permissions:
                for perm_type in permission['types']:
                    perms_to_link.append(
                        role_request_object(role['id'],
                                            self.find_layer_permission_id(permission['name'], perm_type, perms_list))
                    )

            print(perms_to_link)

            # Submit the list
            self.permission_fixture.submit(perms_to_link)

            print(f"The role and user for the email {user['email']} were created successfully!")
        except Exception as error:
            print('Error in process_user:', error)
            raise
