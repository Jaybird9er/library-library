"""added create_book and paginate_books

Revision ID: 3ffd050e0ea0
Revises: 
Create Date: 2025-02-15 10:31:10.702954

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3ffd050e0ea0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "book",
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
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP,
            server_default=sa.text("CURRENT_TIMESTAMP"),
            server_onupdate=sa.text("CURRENT_TIMESTAMP"),
        ),
    )


def downgrade() -> None:
    op.drop_table("book")
