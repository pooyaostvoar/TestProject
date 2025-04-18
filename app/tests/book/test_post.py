from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book_success():
    payload = {
        "title": "book title",
        "author": "book author",
        "isbn": "9781455586691"
    }
    response = client.post("/books", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "book title"
    assert "id" in data