from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.schemas.book import BookRead
from app.schemas.pagination import PaginationParams
from app.services.book import get_all_books

router = APIRouter()


@router.get("/books", response_model=list[BookRead])
def get_books(
    pagination: PaginationParams = Depends(), session: Session = Depends(get_session)
):
    return get_all_books(pagination, session)
