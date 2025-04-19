from sqlmodel import SQLModel, Field, Session
from typing import Optional
from datetime import date

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    published_date: Optional[date] = None
    isbn: Optional[str] = None

    @classmethod
    def create(cls, book_in, session: Session) -> "Book":
        book = cls(**book_in.model_dump())
        session.add(book)
        session.commit()
        session.refresh(book)
        return book