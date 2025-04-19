from fastapi import Query
from pydantic import BaseModel


class PaginationParams(BaseModel):
    offset: int = Query(0, ge=0)
    limit: int = Query(10, ge=1)
