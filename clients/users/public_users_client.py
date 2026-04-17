from httpx import Response
from pydantic import ValidationError

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Client for interacting with /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Method for creating a user.

        :param request: Dictionary with email, password, lastName, firstName and middleName.
        :return: Server response as an httpx.Response object
        """
        return self.post(
            "/api/v1/users",
            json=request.model_dump(by_alias=True)
        )

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    This function creates an instance of PublicUsersClient with a pre-configured HTTP client.

    :return: A ready-to-use PublicUsersClient instance.
    """
    return PublicUsersClient(client=get_public_http_client())
