from fastapi import Depends
from sqlalchemy import literal_column
from sqlalchemy.ext.asyncio import AsyncConnection

from app.database.connection_provider import database_connection
from app.schemas.base import BasePaginationRequest
from app.schemas.book import BookCreateRequest, BookCreateResponse, BookListResponse, BookListResponseItem
from app.models.book import book_table

class BookService:
    def __init__(self, db: AsyncConnection = Depends(database_connection)):
        self.db = db

    async def create_book(self, book: BookCreateRequest) -> BookCreateResponse:
        insert_statement = book_table.insert().values(book.model_dump()).returning(literal_column("*"))
        result_records = await self.db.execute(insert_statement)
        result = result_records.mappings().first()
        response = BookCreateResponse(**result)
        return response
    
    async def paginate(self, list_query: BasePaginationRequest, requesting_path: str) -> list[BookListResponse]:
        if list_query.page > 0:
            previous_page = "{requesting_path}?page={page}&count_per_page={count_per_page}".format(
                requesting_path=requesting_path,
                page=list_query.page - 1,
                count_per_page=list_query.size,                                    
            )
        else:
            previous_page = ""

        next_page = "{requesting_path}?page={page}&count_per_page={count_per_page}".format(
            requesting_path=requesting_path,
            page=list_query.page + 1,
            count_per_page=list_query.size,
        )

        select_statement = book_table.select().limit(list_query.size).offset(list_query.page * list_query.size)
        result_records = await self.db.execute(select_statement)
        records = result_records.mappings().all()
        response = BookListResponse(
            results=[BookListResponseItem(**record) for record in records],
            next=next_page,
            previous=previous_page,
        )
        return response
    
    async def delete_all(self) -> None:
        delete_statement = book_table.delete()
        await self.db.execute(delete_statement)
        return None