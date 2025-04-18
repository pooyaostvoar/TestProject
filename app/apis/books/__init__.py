from fastapi import APIRouter
from app.apis.books.post import router as post_router

router = APIRouter()
router.include_router(post_router)

