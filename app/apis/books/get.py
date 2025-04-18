from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models.book import Book
from app.database import get_session
from app.schemas.book import BookRead
from app.schemas.pagination import PaginationParams

router = APIRouter()

@router.get("/books", response_model=list[BookRead])
def get_books(pagination: PaginationParams = Depends(), session: Session = Depends(get_session)):
    books = session.exec(
        select(Book).offset(pagination.offset).limit(pagination.limit)
    ).all()
    return books

