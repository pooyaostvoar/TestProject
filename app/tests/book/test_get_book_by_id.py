from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def add_book():
    response = client.post(
        "/books",
        json={
            "title": "Book",
            "author": "Author",
        },
    )
    return response.json()


def test_get_book_success():
    book_id = add_book()["id"]
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    assert data["title"] == "Book"
    assert data["author"] == "Author"


def test_get_book_not_found():
    response = client.get("/books/99999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Book not found"
