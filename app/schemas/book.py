from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date
from stdnum import isbn as isbn_check

class BookCreate(BaseModel):
    title: str
    author: str
    published_date: Optional[date] = None
    isbn: Optional[str] = None

    @field_validator("isbn")
    def validate_isbn(cls, v):
        if v and not isbn_check.is_valid(v.replace("-", "")):
            raise ValueError("Invalid ISBN")
        return v

class BookRead(BookCreate):
    id: int