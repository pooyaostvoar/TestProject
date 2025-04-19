from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.database import get_session
from app.errors.book import BookNotFoundError
from app.schemas.book import BookRead, BookCreate
from app.services.book import update_book as update_book_service

router = APIRouter()

@router.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, book_in: BookCreate, session: Session = Depends(get_session)):
    try:
        return update_book_service(book_id, book_in, session)
    except BookNotFoundError:
        raise HTTPException(status_code=404, detail="Book not found")
