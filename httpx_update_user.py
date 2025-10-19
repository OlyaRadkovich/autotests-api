import httpx
from tools.fakers import get_random_email, get_random_password

create_user_payload = {
    "email": get_random_email(),
    "password": get_random_password(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user data:", create_user_response_data)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login data: ", login_response_data)

update_user_header = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}
user_id = create_user_response_data["user"]["id"]

update_user_payload = {
    "email": get_random_email(),
    "password": get_random_password(),
    "lastName": "Basquiat",
    "firstName": "Jean",
    "middleName": "Michel"
}

update_user_response = httpx.patch(
    f"http://127.0.0.1:8000/api/v1/users/{user_id}",
    json=update_user_payload,
    headers=update_user_header
)
update_user_response_data = update_user_response.json()
print("Update user data: ", update_user_response_data)