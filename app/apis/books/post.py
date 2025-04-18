from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.models.book import Book
from app.schemas.book import BookCreate, BookRead

router = APIRouter()

@router.post("/books", response_model=BookRead)
def create_book(book_in: BookCreate, session: Session = Depends(get_session)):
    book = Book(**book_in.model_dump())
    session.add(book)
    session.commit()
    session.refresh(book)
    return book
