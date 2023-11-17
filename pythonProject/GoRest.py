import requests


class GoRestAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def _make_request(self, method, endpoint, params=None, data=None):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.request(method, f"{self.base_url}{endpoint}", headers=headers, params=params, json=data)
        response_data = response.json()
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response_data.get('message', 'Unknown error')}")
        return response_data

    def get_users(self):
        """Get a list of users."""
        endpoint = "/users"
        response_data = self._make_request("GET", endpoint)
        return response_data

    def create_user(self, **user_data):
        """Create a new user."""
        endpoint = "/users"
        response_data = self._make_request("POST", endpoint, data=user_data)
        return response_data

    def update_user(self, user_id, **user_data):
        """Update an existing user."""
        endpoint = f"/users/{user_id}"
        response_data = self._make_request("PUT", endpoint, data=user_data)
        return response_data

    def get_user_by_id(self, user_id):
        """Get a single user by ID."""
        endpoint = f"/users/{user_id}"
        response_data = self._make_request("GET", endpoint)
        return response_data

    def delete_user(self, user_id):
        """Delete a user by ID."""
        endpoint = f"/users/{user_id}"
        response_data = self._make_request("DELETE", endpoint)
        return response_data


if __name__ == "__main__":
    base_url = "https://gorest.co.in/public-api"
    token = "94a8484ee7ceee00d2bb08a6da8014fa5fa7ebe8627bf78251db8ee47d43086a"
    api = GoRestAPI(base_url, token)

    # Get users
    users = api.get_users()
    print("Users:")
    print(users)

    # Create a new user with a unique email
    new_user = api.create_user(name="John Doe", email="john.doe1234@example.com", gender="male", status="active")
    print("New User:")
    print(new_user)

    # Get user IDs
    user_ids = [user['id'] for user in users.get('data', [])]

    # Update an existing user with a unique email
    if user_ids:
        user_id_to_update = user_ids[0]
        updated_user = api.update_user(user_id_to_update, name="Updated Name", email="updated.email@example.com",
                                       gender="female", status="inactive")
        print("Updated User:")
        print(updated_user)
    else:
        print("No users found for updating.")

    # Get a single user by ID (replace user_id_to_get with an actual user ID)
    if user_ids:
        user_id_to_get = user_ids[0]
        single_user = api.get_user_by_id(user_id_to_get)
        print("Single User:")
        print(single_user)
    else:
        print("No users found for getting by ID.")

        # Delete a user (replace user_id_to_delete with an actual user ID)
    if user_ids:
        user_id_to_delete = user_ids[0]
        deleted_user = api.delete_user(user_id_to_delete)
        print("Deleted User:")
        print(deleted_user)
    else:
        print("No users found for deletion.")