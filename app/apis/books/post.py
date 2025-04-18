from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.models.book import Book

router = APIRouter()

@router.post("/books", response_model=Book)
def create_book(book: Book, session: Session = Depends(get_session)):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book
