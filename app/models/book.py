from sqlmodel import SQLModel, Field, Session,update
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

    @classmethod
    def update_book(cls, book_id: int, book_in, session: Session) -> Optional["Book"]:
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
        return  result.scalar_one_or_none()