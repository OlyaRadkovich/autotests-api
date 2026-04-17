from httpx import Response
from clients.api_client import APIClient
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, \
    CreateCourseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class CoursesClient(APIClient):
    """
    Client for interacting with /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Method to get a list of courses.

        :param query: Dictionary with userId.
        :return: Server response as an httpx.Response object
        """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Method to get a course.

        :param course_id: Course identifier.
        :return: Server response as an httpx.Response object
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Method to create a course.

        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Server response as an httpx.Response object
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Method to update a course.

        :param course_id: Course identifier.
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime.
        :return: Server response as an httpx.Response object
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Method to delete a course.

        :param course_id: Course identifier.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Function creates an instance of CoursesClient with an already configured HTTP client.

    :return: Ready-to-use CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
