from pydantic import BaseModel, field_serializer, HttpUrl

from app.models.book import Book
from app.schemas.base import BaseListResponse

class BookCreateRequest(BaseModel):
    book_id: int
    title: str
    image: HttpUrl | None = None
    author_fam_name: str
    author_1st_name: str
    isbn: str
    publication_date: int
    genre: str
    stock: int | None = 0
    bookcase_ID: int
    price: int

    @field_serializer("image")
    def validate_image(self, image: HttpUrl, _info):
        return str(image)

# class BookCreateRequest(Book):
#     pass
    
class BookCreateResponse(Book):
    pass

class BookListResponseItem(Book):
    pass

class BookListResponse(BaseListResponse):
    results: list[BookListResponseItem]