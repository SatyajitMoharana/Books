from fastapi import APIRouter
from src.api.v1.endpoints import book as book_router
router = APIRouter()

# Reporting endpoints with distinct prefixes
router.include_router(
    book_router.router, prefix="/books", tags=["books"]
)
