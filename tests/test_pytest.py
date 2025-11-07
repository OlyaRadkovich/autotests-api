import pytest


class TestFirstTestClass:
    def test_first_try(self):
        print("Hello, World?")

    def test_second_try(self):
        pass


def test_assert_positive_case():
    x, y = 6, 9
    assert (y - 3) == 6, "y - 3 not equals to x"


def test_assert_negative_case():
    x, y = 6, 9
    assert (y - y) == 6, "y - y not equals to x"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
