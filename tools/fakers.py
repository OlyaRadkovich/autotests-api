import time
import random

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

def get_random_password() -> str:
    random_pass = ""
    symbols = "!@#$%^&*()1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    lenght = len(symbols)
    for _ in range(16):
        random_pass+=symbols[random.randint(0,lenght-1)]
    return random_pass
