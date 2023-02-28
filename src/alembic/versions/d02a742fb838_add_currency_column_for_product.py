"""add currency column for product

Revision ID: d02a742fb838
Revises: f8dad8924503
Create Date: 2023-02-28 14:58:37.069677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd02a742fb838'
down_revision = 'f8dad8924503'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('products', sa.Column('currency', sa.String(3), nullable=True))


def downgrade() -> None:
    op.drop_column('products', 'currency')
