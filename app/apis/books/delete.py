from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, delete
from app.database import get_session
from app.models.book import Book

router = APIRouter()

@router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, session: Session = Depends(get_session)):
    result = session.exec(
        delete(Book)
        .where(Book.id == book_id)
        .returning(Book)
    )

    deleted_book = result.scalar_one_or_none()

    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    session.commit()
