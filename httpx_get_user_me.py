import httpx

login_payload = {
  "email": "iggy_pop@example.com",
  "password": "blahblahblah"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data=login_response.json()

print("Login response: ", login_response_data)
print("Status code: ", login_response.status_code)

access_token = login_response_data['token']['accessToken']
headers = {"Authorization": f"Bearer {access_token}"}
response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)

print("Get user response:", response.json())
print("Get user status code:", response.status_code)