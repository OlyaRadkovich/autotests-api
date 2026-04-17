from httpx import Response
from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """
    Client for interacting with /api/v1/authentication
    """

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Method performs user authentication.

        :param request: Dictionary with email and password.
        :return: Server response as an httpx.Response object
        """
        return self.post(
            "/api/v1/authentication/login",
            json=request.model_dump(by_alias=True)
        )

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Method refreshes the authorization token.

        :param request: Dictionary with refreshToken.
        :return: Server response as an httpx.Response object
        """
        return self.post(
            "/api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    This function creates an instance of AuthenticationClient with a pre-configured HTTP client.

    :return: A ready-to-use AuthenticationClient instance.
    """
    return AuthenticationClient(client=get_public_http_client())
