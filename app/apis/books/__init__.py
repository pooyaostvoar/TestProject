from fastapi import APIRouter
from app.apis.books.post import router as post_router
from app.apis.books.get  import router as get_router
from app.apis.books.get_book_by_id import router as get_book_router
from app.apis.books.put import router as put_router

router = APIRouter()
router.include_router(post_router)
router.include_router(get_router)
router.include_router(get_book_router)
router.include_router(put_router)