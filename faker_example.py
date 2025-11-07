import time
import random
from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())
print(fake.email())

data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

print(data)

# custom fakers
def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


def get_random_password() -> str:
    random_pass = ""
    symbols = "!@#$%^&*()1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    lenght = len(symbols)
    for _ in range(16):
        random_pass += symbols[random.randint(0, lenght - 1)]
    return random_pass