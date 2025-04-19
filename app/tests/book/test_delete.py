from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_delete_book_success():
    response = client.post(
        "/books",
        json={"title": "Test Book", "author": "Test Author", "isbn": "9781455586691"},
    )
    book_id = response.json()["id"]

    delete_response = client.delete(f"/books/{book_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/books/{book_id}")
    assert get_response.status_code == 404


def test_delete_book_not_found():
    response = client.delete("/books/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"
