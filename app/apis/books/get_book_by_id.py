from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.database import get_session
from app.models.book import Book
from app.schemas.book import BookRead

router = APIRouter()


@router.get("/books/{book_id}", response_model=BookRead)
def get_book_by_id(book_id: int, session: Session = Depends(get_session)):
    query = select(Book).where(Book.id == book_id)
    book = session.exec(query).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book
