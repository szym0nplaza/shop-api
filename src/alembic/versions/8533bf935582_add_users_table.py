"""add users table

Revision ID: 8533bf935582
Revises: 
Create Date: 2023-02-25 13:59:11.792667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8533bf935582"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "groups",
        sa.Column("name", sa.String(50), unique=True, primary_key=True),
        sa.Column(
            "perms",
            sa.String(1000),
        ),
    )

    op.execute(
        "INSERT INTO groups (name, perms) VALUES ('admin', '__all__'), ('seller', 'manage_product,view_product,manage_user,view_user'), ('customer', 'manage_order,view_order,manage_user,view_user')"
    )

    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("surname", sa.String(50), nullable=False),
        sa.Column("email", sa.String(100), nullable=False, unique=True),
        sa.Column("group", sa.String(30), nullable=True),
        sa.Column("password", sa.LargeBinary(), nullable=False),
        sa.ForeignKeyConstraint(["group"], ["groups.name"], ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("groups")
