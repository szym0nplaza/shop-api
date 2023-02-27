"""add prodcuts and orders table

Revision ID: 43b669712253
Revises: 8533bf935582
Create Date: 2023-02-27 14:19:11.395436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43b669712253'
down_revision = '8533bf935582'
branch_labels = None
depends_on = '8533bf935582'


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("owner_id", sa.Integer),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("price", sa.DECIMAL(precision=20, scale=2), nullable=False),
        sa.ForeignKeyConstraint(["owner_id"], ["users.id"], ondelete="CASCADE"),
    )

    op.create_table(
        "orders",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("date", sa.DateTime, nullable=False),
        sa.Column("status", sa.String(50), nullable=True),
        sa.Column("user_id", sa.Integer),
        sa.Column("product_id", sa.Integer),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_table("orders")
    op.drop_table("products")
