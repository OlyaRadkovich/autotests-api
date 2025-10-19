import httpx
from tools.fakers import get_random_email, get_random_password

payload = {
    "email": get_random_email(),
    "password": get_random_password(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=payload)
print("Create user response:", response.json())
print("Create user status code:", response.status_code)
