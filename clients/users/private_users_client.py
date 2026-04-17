from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
    """
    Client for interacting with /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Method for getting the current user.

        :return: Server response as an httpx.Response object
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Method for getting a user by ID.

        :param user_id: User ID.
        :return: Server response as an httpx.Response object
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Method for updating a user by ID.

        :param user_id: User ID.
        :param request: Dictionary with email, lastName, firstName, middleName.
        :return: Server response as an httpx.Response object
        """
        return self.patch(
            f"/api/v1/users/{user_id}",
            json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Method for deleting a user by ID.

        :param user_id: User ID.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    This function creates an instance of PrivateUsersClient with a pre-configured HTTP client.

    :return: A ready-to-use PrivateUsersClient instance.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
