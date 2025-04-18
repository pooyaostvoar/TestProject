# API Documentation

This directory contains documentation for the available API endpoints.

For full interactive documentation and the ability to test each endpoint, visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## [📚 `POST /books`](http://127.0.0.1:8000/docs#/default/create_book_books_post)

Creates a new book entry.

### Request Body

```json
{
  "title": "The Deep Work",
  "author": "Cal Newport",
  "published_date": "2025-04-18",
  "isbn": "978-3-16-148410-0"
}
```

All fields are required except `published_date` and `isbn`.

### Response

- **Status Code:** `200 OK`
- **Body:**

```json
{
  "id": 1,
  "title": "The Deep Work",
  "author": "Cal Newport",
  "published_date": "2025-04-18",
  "isbn": "978-3-16-148410-0"
}
```

### Errors

- **`422 Unprocessable Entity`**  
  If required fields are missing or validation fails.

  Example:
  ```json
  {
    "detail": [
      {
        "loc": ["body", "title"],
        "msg": "Field required",
        "type": "value_error.missing"
      }
    ]
  }
  ```

  Invalid ISBN example:
  ```json
  {
    "detail": [
      {
        "loc": ["body", "isbn"],
        "msg": "Value error, Invalid ISBN",
        "type": "value_error"
      }
    ]
  }
  ```

---

More endpoints will be documented soon. For now, check `/docs` for full details.