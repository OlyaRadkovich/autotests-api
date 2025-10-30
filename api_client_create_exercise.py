from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import FilesClient, CreateFileRequestDict, get_files_client
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, PublicUsersClient, CreateUserRequestDict
from tools.fakers import get_random_email, get_random_password

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password=get_random_password(),
    lastName="string",
    firstName="string",
    middleName="string"
)

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename='nice_image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print("Create file data: ", create_file_response)

courses_client = get_courses_client(authentication_user)

create_course_request = CreateCourseRequestDict(
    title='API testing with Python',
    maxScore=1300,
    minScore=10,
    description='The best API testing course ever',
    estimatedTime='2 months',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print("Create course data: ", create_course_response)

exercise_client = get_exercises_client(authentication_user)
create_exercise_request = CreateExerciseRequestDict(
    title='Work with gRPC',
    courseId=create_course_response['course']['id'],
    maxScore=10,
    minScore=0,
    orderIndex=3,
    description='Work with gRPC. Practice',
    estimatedTime='1 day'
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print("Create exercise data: ", create_exercise_response)
