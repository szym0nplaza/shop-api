"""add stripe_id column for user

Revision ID: f8dad8924503
Revises: 43b669712253
Create Date: 2023-02-27 21:56:03.900345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8dad8924503'
down_revision = '43b669712253'
branch_labels = None
depends_on = '8533bf935582'


def upgrade() -> None:
    op.add_column('users', sa.Column('stripe_id', sa.String(200), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'stripe_id')
