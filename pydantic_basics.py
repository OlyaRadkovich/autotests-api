"""
"course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
"""
import uuid

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel

from tools.fakers import get_random_email


class UserSchemaV2(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default="user-id")
    email: EmailStr = Field(default_factory=get_random_email)
    last_name: str = Field(alias="lastName", default="Doe")
    first_name: str = Field(alias="firstName", default="John")
    middle_name: str = Field(alias="middleName", default="")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @computed_field(alias="userData")
    def user_data(self) -> str:
        return f"{self.first_name} {self.last_name}, email: {self.email}"


class FileSchemaV2(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default="test-file-id")
    filename: str = Field(default="nice_image.png")
    directory: str = Field(default="courses")
    url: HttpUrl = Field(default="http://localhost:8080")


class CourseSchemaV2(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel,
                              populate_by_name=True)  # to_camel - способ указать алиас, когда уверены, что в апи все ключи в camel case

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)  # предпочтительный способ указать алиас
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    preview_file: FileSchemaV2 = Field(alias="previewFile", default_factory=FileSchemaV2)
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchemaV2 = Field(alias="createdByUser", default_factory=UserSchemaV2)


course_default_model = CourseSchemaV2(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileSchemaV2(
        id="file-id",
        filename="image.png",
        directory="courses",
        url="http://localhost:8000"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchemaV2(
        id="user-id",
        email="user@example.com",
        lastName="Ford",
        firstName="Henry",
        middleName="James"
    )
)
print("Course default model: ", course_default_model)

course_dict = {
    "id": "course-id",
    "title": "Selenium",
    "maxScore": 100,
    "minScore": 10,
    "description": "Selenium",
    "previewFile": {
        "id": "file-id",
        "filename": "image.png",
        "directory": "courses",
        "url": "http://localhost:8000"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@example.com",
        "lastName": "Ford",
        "firstName": "Henry",
        "middleName": "James"
    }
}

course_dict_model = CourseSchemaV2(**course_dict)
print("Course dict model: ", course_dict_model)

course_json = """
{
    "id": "course-id",
    "title": "Pydantic",
    "maxScore": 100,
    "minScore": 10,
    "description": "Pydantic",
        "previewFile": {
        "id": "file-id",
        "filename": "image.png",
        "directory": "courses",
        "url": "http://localhost:8000"
    },
    "estimatedTime": "1 week",
        "createdByUser": {
        "id": "user-id",
        "email": "user@example.com",
        "lastName": "Ford",
        "firstName": "Henry",
        "middleName": "James"
    }
}
"""

course_json_model = CourseSchemaV2.model_validate_json(course_json)
print("Course json model: ", course_json_model)
print("Course json model dump: ", course_json_model.model_dump(by_alias=True))
print("Course json model dump json: ", course_json_model.model_dump_json())

course1 = CourseSchemaV2()
course2 = CourseSchemaV2()
print(course1.created_by_user.email)
print(course2.created_by_user.email)

user = UserSchemaV2()
print(user.user_data, user.get_username())

try:
    file = FileSchemaV2(
        id="file-id",
        filename="image.png",
        directory="courses",
        url="local"
    )
except ValidationError as e:
    print(f"Ошибка: {e}")
