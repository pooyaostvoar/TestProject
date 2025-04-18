from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, update
from app.database import get_session
from app.models.book import Book
from app.schemas.book import BookRead, BookCreate

router = APIRouter()

@router.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, book_in: BookCreate, session: Session = Depends(get_session)):

    result = session.exec(
        update(Book)
        .where(Book.id == book_id)
        .values(
            title=book_in.title,
            author=book_in.author,
            isbn=book_in.isbn,
            published_date=book_in.published_date
        )
        .returning(Book)
    )

    updated_book = result.scalar_one_or_none()

    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book
