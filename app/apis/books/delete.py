from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.database import get_session
from app.errors.book import BookNotFoundError
from app.services.book import delete_book_by_id

router = APIRouter()

@router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, session: Session = Depends(get_session)):
    try:
        return delete_book_by_id(book_id, session)
    except BookNotFoundError:
        raise HTTPException(status_code=404, detail="Book not found")
