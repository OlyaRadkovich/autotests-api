import httpx
from faker_example import get_random_email, get_random_password
from tools.fakers import fake

payload = {
    "email": get_random_email(),
    "password": get_random_password(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.middle_name()
}

response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=payload)
print("Create user response:", response.json())
print("Create user status code:", response.status_code)
