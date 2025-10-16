import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

data = {
    "title": "new task",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)
print(response.request.headers)
print(response.json())

data = {
    "username": "new task",
    "password": "654321",
}

response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.request.headers)
print(response.json())

headers = {"Authorization": "Bearer very_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.request.headers)
print(response.json())

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)
print(response.json())

files = {"file": ("my_example.txt", open("my_example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/2")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/22")

print(response1.json())
print(response2.json())

client = httpx.Client(headers={"Authorization": "Bearer very_secret_token"})
response = client.get("https://httpbin.org/get")

print(response.json())
print(response.request.headers)

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Request error: {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Request exceeded time limit")
