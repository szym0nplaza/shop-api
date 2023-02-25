"""add users table

Revision ID: 8533bf935582
Revises: 
Create Date: 2023-02-25 13:59:11.792667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8533bf935582'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('surname', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('group', sa.String(30), nullable=True),
        sa.Column('password', sa.LargeBinary(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
