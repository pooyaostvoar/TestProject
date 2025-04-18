from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    published_date: Optional[date] = None
    isbn: Optional[str] = None
