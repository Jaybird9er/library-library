from fastapi import APIRouter, Depends

from app.schemas.base import BasePaginationRequest
from app.schemas.book import (
    BookCreateRequest, 
    BookCreateResponse,
    BookListResponse
)
from app.services.book import BookService
from app.settings import Settings

router = APIRouter(tags=["books"])

settings = Settings()

@router.post("/")
async def create_book(
    book: BookCreateRequest,
    book_service: BookService = Depends(BookService),
) -> BookCreateResponse:
    return await book_service.create_book(book)

@router.get("/")
async def paginate_books(
    pagination_query: BasePaginationRequest = Depends(BasePaginationRequest),
    book_service: BookService = Depends(BookService),
) -> BookListResponse:
    return await book_service.paginate(
        pagination_query, 
        requesting_path="{public_base_url}/books".format(public_base_url=settings.public_base_url)
    )

@router.delete("/")
async def delete_all_books(
    book_service: BookService = Depends(BookService),
) -> None:
    return await book_service.delete_all()