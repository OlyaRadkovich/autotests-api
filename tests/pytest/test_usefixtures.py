import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Deleting all data from DB")


@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Creating new data in DB")

@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...