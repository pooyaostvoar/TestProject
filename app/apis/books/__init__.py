from fastapi import APIRouter
from app.apis.books.post import router as post_router
from app.apis.books.get  import router as get_router

router = APIRouter()
router.include_router(post_router)
router.include_router(get_router)
