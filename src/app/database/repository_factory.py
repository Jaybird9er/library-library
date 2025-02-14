from fastapi import Depends
from sqlalchemy.ext.asyncio.engine import AsyncConnection

from app.database import Repository, SqlAlchemyRepository
from app.database.connection_provider import database_connection
from app.models.product import product_table


def get_product_repository(db: AsyncConnection = Depends(database_connection)) -> Repository:
    return SqlAlchemyRepository(db=db, table=product_table)
