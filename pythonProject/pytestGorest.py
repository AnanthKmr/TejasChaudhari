# import pytest
# from GoRest import GoRestAPI
# import allure
#
# BASE_URL = "https://gorest.co.in/public-api"
# TOKEN = "94a8484ee7ceee00d2bb08a6da8014fa5fa7ebe8627bf78251db8ee47d43086a"
#
#
# @pytest.fixture
# def api_instance():
#     return GoRestAPI(BASE_URL, TOKEN)
#
#
# def test_get_users(api_instance):
#     users = api_instance.get_users()
#     print("Get Users Response:")
#     print(users)
#     assert users['code'] == 200
#     assert 'data' in users
#
#
# def test_create_user(api_instance):
#     new_user_data = {
#         "name": "Test User",
#         "email": "test.user12@example.com",
#         "gender": "female",
#         "status": "active"
#     }
#     new_user = api_instance.create_user(**new_user_data)
#     print("Create User Response:")
#     print(new_user)
#     assert new_user['code'] == 201
#     assert 'data' in new_user
#
#     # Additional: Check if the newly created user is in the list
#     users = api_instance.get_users()
#     print("Get Users After Create User:")
#     print(users)
#     assert any(user['email'] == new_user_data['email'] for user in users.get('data', []))
#
#
# def test_update_user(api_instance):
#     users = api_instance.get_users()
#     if 'data' in users and users['data']:
#         user_id_to_update = users['data'][0]['id']
#         updated_user_data = {
#             "name": "Updated Test User",
#             "email": "updated.test.user@example.com",
#             "gender": "male",
#             "status": "inactive"
#         }
#         updated_user = api_instance.update_user(user_id_to_update, **updated_user_data)
#         print("Update User Response:")
#         print(updated_user)
#         assert updated_user['code'] == 200
#         assert 'data' in updated_user
#
#         # Additional: Check if the user's data is properly updated
#         single_user = api_instance.get_user_by_id(user_id_to_update)
#         print("Get User by ID After Update:")
#         print(single_user)
#         assert single_user['code'] == 200
#         assert 'data' in single_user
#         assert single_user['data']['name'] == updated_user_data['name']
#         assert single_user['data']['email'] == updated_user_data['email']
#
#
# def test_get_user_by_id(api_instance):
#     users = api_instance.get_users()
#     if 'data' in users and users['data']:
#         user_id_to_get = users['data'][0]['id']
#         single_user = api_instance.get_user_by_id(user_id_to_get)
#         print("Get User by ID Response:")
#         print(single_user)
#         assert single_user['code'] == 200
#         assert 'data' in single_user
#
#
# def test_delete_user(api_instance):
#     users = api_instance.get_users()
#     if 'data' in users and users['data']:
#         user_id_to_delete = users['data'][0]['id']
#         deleted_user = api_instance.delete_user(user_id_to_delete)
#         print("Delete User Response:")
#         print(deleted_user)
#         assert deleted_user['code'] == 204
#         assert not deleted_user.get('data', [])  # Expecting an empty 'data' field for a successful deletion
#
#         # Additional: Check if the user is no longer in the list after deletion
#         users_after_deletion = api_instance.get_users()
#         print("Get Users After Delete User:")
#         print(users_after_deletion)
#         assert all(user['id'] != user_id_to_delete for user in users_after_deletion.get('data', []))


import pytest
from GoRest import GoRestAPI

BASE_URL = "https://gorest.co.in/public-api"
TOKEN = "94a8484ee7ceee00d2bb08a6da8014fa5fa7ebe8627bf78251db8ee47d43086a"


@pytest.fixture
def api_instance():
    return GoRestAPI(BASE_URL, TOKEN)


class TestUserManagement:

    @pytest.mark.usefixtures("api_instance")
    def test_get_users(self, api_instance):
        # Test to retrieve users and assert the response code and data existence
        users = api_instance.get_users()
        assert users['code'] == 200
        assert 'data' in users

    @pytest.mark.usefixtures("api_instance")
    def test_create_user(self, api_instance):
        # Test to create a new user, assert the response code and data existence
        new_user_data = {
            "name": "Test User",
            "email": "test.user12@example.com",
            "gender": "female",
            "status": "active"
        }
        new_user = api_instance.create_user(**new_user_data)
        assert new_user['code'] == 201
        assert 'data' in new_user
        # Additional: Check if the newly created user is in the list
        users = api_instance.get_users()
        assert any(user['email'] == new_user_data['email'] for user in users.get('data', []))

    @pytest.mark.usefixtures("api_instance")
    def test_update_user(self, api_instance):
        # Test to update an existing user and assert the response code and data existence
        users = api_instance.get_users()
        if 'data' in users and users['data']:
            user_id_to_update = users['data'][0]['id']
            updated_user_data = {
                "name": "Updated Test User",
                "email": "updated.test.user@example.com",
                "gender": "male",
                "status": "inactive"
            }
            updated_user = api_instance.update_user(user_id_to_update, **updated_user_data)
            assert updated_user['code'] == 200
            assert 'data' in updated_user
            # Additional: Check if the user's data is properly updated
            single_user = api_instance.get_user_by_id(user_id_to_update)
            assert single_user['code'] == 200
            assert 'data' in single_user
            assert single_user['data']['name'] == updated_user_data['name']
            assert single_user['data']['email'] == updated_user_data['email']

    @pytest.mark.usefixtures("api_instance")
    def test_get_user_by_id(self, api_instance):
        # Test to get a user by ID and assert the response code and data existence
        users = api_instance.get_users()
        if 'data' in users and users['data']:
            user_id_to_get = users['data'][0]['id']
            single_user = api_instance.get_user_by_id(user_id_to_get)
            assert single_user['code'] == 200
            assert 'data' in single_user

    @pytest.mark.usefixtures("api_instance")
    def test_delete_user(self, api_instance):
        # Test to delete a user and assert the response code and absence of data
        users = api_instance.get_users()
        if 'data' in users and users['data']:
            user_id_to_delete = users['data'][0]['id']
            deleted_user = api_instance.delete_user(user_id_to_delete)
            assert deleted_user['code'] == 204
            assert not deleted_user.get('data', [])
            # Additional: Check if the user is no longer in the list after deletion
            users_after_deletion = api_instance.get_users()
            assert all(user['id'] != user_id_to_delete for user in users_after_deletion.get('data', []))
