import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
     print("[AUTOUSE] Send data to the analytical service")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Initiate autotests settings")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Create user data one time for a test class")


@pytest.fixture(autouse=True)
def users_client(settings):
     print("[FUNCTION] Create API client for each function")


class TestUserFlow:
    def test_user_can_login(self, settings, user):
        ...

    def test_user_can_create_course(self, settings, user):
        ...


class TestAccountFlow:
    def test_user_account(self,settings, user):
        ...


@pytest.fixture
def user_data() -> dict:
    print("Creating user before test (setup)")
    yield {"username": "test_user", "email": "test@example.com"}
    print("Deleting user after test (teardown)")


def test_user_email(user_data: dict):
    print(user_data)
    assert user_data['email'] == "test@example.com"


def test_user_username(user_data: dict):
    print(user_data)
    assert user_data['username'] == "test_user"