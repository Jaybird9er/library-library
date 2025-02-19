import sqlalchemy as sa
from pydantic import BaseModel, Field, HttpUrl
from app.models import MetaData

metadata = MetaData()

class Book(BaseModel):
    book_id: int = Field(primary_key=True)
    title: str
    image: HttpUrl | None
    author_fam_name: str
    author_1st_name: str
    isbn: str
    publication_date: int
    genre: str
    stock: int | None
    bookcase_ID: int
    price: int

    # @field_serializer("image")
    # def validate_image(self, image: HttpUrl, _info):
    #     return str(image)

book_table = sa.Table(
    "book",
    metadata,
    sa.Column("book_id", sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column("title", sa.Unicode(255), index=True, nullable=False),
    sa.Column("author_fam_name", sa.Unicode(255), index=True, nullable=False),
    sa.Column("author_1st_name", sa.Unicode(255), index=True, nullable=False),
    sa.Column("isbn", sa.VARCHAR(17), index=True, nullable=False, unique=True),
    sa.Column("publication_date", sa.Integer, index=True, nullable=False),
    sa.Column("genre", sa.VARCHAR(55), index=True, nullable=False),
    sa.Column("stock", sa.SmallInteger, index=True, nullable=False, default=1),
    sa.Column("bookcase_ID", sa.SmallInteger),
    sa.Column("price", sa.Integer, index=True, nullable=False, default=1000),
    sa.Column("image", sa.String(1024), nullable=False),
)