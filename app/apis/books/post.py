from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.schemas.book import BookCreate, BookRead
from app.services.book import create_book as create_book_service

router = APIRouter()


@router.post("/books", response_model=BookRead)
def create_book(book_in: BookCreate, session: Session = Depends(get_session)):
    return create_book_service(book_in, session)
