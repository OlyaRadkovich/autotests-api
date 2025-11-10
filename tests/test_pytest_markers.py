import pytest

# examples
# pytest -v -s -k "test_pytest_markers"
# pytest -m smoke
# pytest -s -v -m "regression or api and not critical"

SYSTEM_VERSION = "v1.2.0"


@pytest.mark.skip(reason="feature is in developing")
def test_smoke_case():
    assert 1 + 1 == 2


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",
    reason="test cannot run on v1.2.0"
)
@pytest.mark.regression
def test_regression_case():
    assert 2 * 2 == 4


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.5",
    reason="test cannot run on v1.2.5"
)
@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    def test_logout(self):
        ...


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...


@pytest.mark.api
class TestUserInterface:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login(self):
        ...

    @pytest.mark.xfail(reason="There's a bug, see Jira task #...")
    @pytest.mark.regression
    def test_forgot_password(self):
        assert 2 == 3

    @pytest.mark.xfail(reason="There's a bug, see Jira task #...")
    @pytest.mark.smoke
    def test_signup(self):
        ...
