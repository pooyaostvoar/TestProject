from typing import Optional, Sequence

from sqlmodel import Session

from app.errors.book import BookNotFoundError
from app.models.book import Book
from app.schemas.book import BookCreate
from app.schemas.pagination import PaginationParams


def create_book(book_in: BookCreate, session: Session) -> Book:
    return Book.create(book_in, session)

def update_book(book_id: int, book_in, session: Session) -> Optional[Book]:
    updated_book = Book.update_book(book_id, book_in, session)
    if updated_book is None:
        raise BookNotFoundError()

    session.commit()

    return updated_book

def get_all_books(pagination: PaginationParams, session:Session)-> Sequence[Book]:
    return Book.get_all(pagination, session)

def get_book_by_id(book_id:int, session:Session)->Optional[Book]:
    book = Book.get_book_by_id(book_id, session)

    if book is None:
        raise BookNotFoundError()

    return book

def delete_book_by_id(book_id:int, session:Session)->Optional[Book]:
    deleted_book = Book.delete_book_by_id(book_id, session)

    if deleted_book is None:
        raise  BookNotFoundError()

    session.commit()

    return deleted_book