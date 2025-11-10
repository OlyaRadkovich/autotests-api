import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest) -> str:
    return request.param


def test_host(host: str):
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("user", ["Alina", "Zina"])
class TestOperation:
    def test_user_with_operation(self, user):
        print(f"User with operation: {user}")

    def test_user_without_operation(self, user):
        print(f"User without operation: {user}")


users = {
    "+375000000011": "User with a positive account balance",
    "+375000000022": "User with a zero account balance",
    "+375000000033": "User with a blocked account"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    pass


@pytest.mark.parametrize(
    "code, body",
    [(200, {"ok": True}), (400, {"error": "bad"})],
    ids=lambda p: f"status={p}"
)
def test_api(code, body):
    ...


@pytest.mark.parametrize("x", [0, 1, 2], ids=lambda v: "zero" if v == 0 else None)
def test_mixed_ids(x):
    ...