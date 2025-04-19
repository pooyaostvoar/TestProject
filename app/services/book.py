from typing import Optional

from sqlmodel import Session

from app.errors.book import BookNotFoundError
from app.models.book import Book
from app.schemas.book import BookCreate

def create_book(book_in: BookCreate, session: Session) -> Book:
    return Book.create(book_in, session)

def update_book(book_id: int, book_in, session: Session) -> Optional["Book"]:
    updated_book = Book.update_book(book_id, book_in, session)
    if updated_book is None:
        raise BookNotFoundError()

    session.commit()

    return updated_book

