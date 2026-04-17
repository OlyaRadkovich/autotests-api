from httpx import Response
from clients.api_client import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class FilesClient(APIClient):
    """
    Client for working with /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Method for getting a file.

        :param file_id: File identifier.
        :return: Server response as an httpx.Response object
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Method for creating a file.

        :param request: Dictionary with filename, directory, upload_file.
        :return: Server response as an httpx.Response object
        """
        return self.post(
            "/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={"upload_file"}),
            files={"upload_file": open(request.upload_file, 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Method for deleting a file.

        :param file_id: File identifier.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    The function creates an instance of FilesClient with an already configured HTTP client.

    :return: Ready-to-use FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
