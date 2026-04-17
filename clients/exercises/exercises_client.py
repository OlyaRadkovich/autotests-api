from httpx import Response
from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, \
    UpdateExerciseResponseSchema

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class ExercisesClient(APIClient):
    """
    Client for interacting with /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Method for getting a list of course exercises.

        :param query: Dictionary with courseId.
        :return: Server response as an httpx.Response object
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Method for getting an exercise.

        :param exercise_id: Exercise ID.
        :return: Server response as an httpx.Response object
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Method for creating an exercise.

        :param request: Dictionary with title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Server response as an httpx.Response object
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exrecise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Method for updating an exercise.

        :param exercise_id: Exercise ID.
        :param request: Dictionary with title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Server response as an httpx.Response object
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id) -> Response:
        """
        Method for deleting an exercise.

        :param exercise_id: Exercise ID.
        :return: Server response as an httpx.Response object
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query.model_dump(by_alias=True))
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exrecise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    This function creates an instance of ExercisesClient with a pre-configured HTTP client.

    :return: A ready-to-use ExercisesClient instance.
    """
    return ExercisesClient(client=get_private_http_client(user))
