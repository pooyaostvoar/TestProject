import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def setup_book():
    response = client.post("/books", json={
        "title": "Deep Work",
        "author": "Cal Newport",
        "isbn": "9781455586691",
        "published_date": "2025-04-18"
    })
    book = response.json()
    return book

def test_update_book_success(setup_book):
    book_id = setup_book["id"]
    updated_data = {
        "title": "Updated Book Title",
        "author": "Updated Author",
        "isbn": "978-3-16-148410-0",
        "published_date": "2025-04-18"
    }
    response = client.put(f"/books/{book_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Book Title"
    assert data["author"] == "Updated Author"
    assert data["isbn"] == "978-3-16-148410-0"

def test_update_book_not_found():
    updated_data = {
        "title": "Nonexistent Book",
        "author": "Unknown Author",
        "isbn": "978-3-16-148410-0",
        "published_date": "2025-04-18"
    }
    response = client.put("/books/999", json=updated_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_update_book_with_invalid_isbn():
    response = client.put("/books/1", json={
        "title":"title",
        "author": "author",
        "isbn": "9781455586691-invalid"
    })
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'Value error, Invalid ISBN'