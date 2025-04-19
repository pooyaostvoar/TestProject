from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.database import get_session
from app.errors.book import BookNotFoundError
from app.schemas.book import BookRead
from app.services.book import get_book_by_id as get_book_by_id_service
router = APIRouter()


@router.get("/books/{book_id}", response_model=BookRead)
def get_book_by_id(book_id: int, session: Session = Depends(get_session)):
    try:
        return get_book_by_id_service(book_id, session)
    except BookNotFoundError:
        raise HTTPException(status_code=404, detail="Book not found")