from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema
from clients.users.public_users_client import get_public_users_client

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="nice_image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print("Create file data: ", create_file_response)

courses_client = get_courses_client(authentication_user)

create_course_request = CreateCourseRequestSchema(
    title="API testing with Python",
    max_score=1300,
    min_score=10,
    description="The best API testing course ever",
    estimated_time="2 months",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print("Create course data: ", create_course_response)

exercise_client = get_exercises_client(authentication_user)
create_exercise_request = CreateExerciseRequestSchema(
    title="Work with gRPC",
    course_id=create_course_response.course.id,
    max_score=10,
    min_score=0,
    order_index=3,
    description="Work with gRPC. Practice",
    estimated_time="1 day"
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print("Create exercise data: ", create_exercise_response)
