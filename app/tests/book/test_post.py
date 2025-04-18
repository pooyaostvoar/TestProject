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

def test_create_book_with_out_title():
    response = client.post("/books", json={
        "author": "author",
        "isbn": "9781455586691"
    })
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'Field required'

def test_create_book_with_invalid_isbn():
    response = client.post("/books", json={
        "title":"title",
        "author": "author",
        "isbn": "9781455586691-invalid"
    })
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'Value error, Invalid ISBN'