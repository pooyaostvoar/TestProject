import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def setup_books():
    for i in range(10):
        client.post(
            "/books",
            json={
                "title": f"Book {i}",
                "author": f"Author {i}",
            },
        )


def test_get_books_with_pagination_limit_5_offset_0():
    response = client.get("/books?limit=5&offset=0")
    assert response.status_code == 200

    books = response.json()
    assert isinstance(books, list)
    assert len(books) == 5
    assert books[0]["title"] == "Book 0"


def test_get_books_with_pagination_offset_beyond_range():
    response = client.get("/books?limit=5&offset=11")
    assert response.status_code == 200

    books = response.json()
    assert isinstance(books, list)
    assert len(books) == 0
