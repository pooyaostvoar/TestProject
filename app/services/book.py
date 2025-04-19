from sqlmodel import Session
from app.models.book import Book
from app.schemas.book import BookCreate

def create_book(book_in: BookCreate, session: Session) -> Book:
    return Book.create(book_in, session)
