"""005_add_users

Revision ID: 6c08283bd8e7
Revises: 13986dd17c3e
Create Date: 2025-03-04 09:32:28.885198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c08283bd8e7'
down_revision: Union[str, None] = '13986dd17c3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column('id', sa.BigInteger, nullable=False),
        sa.Column('email', sa.String, unique=True),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('active', sa.Boolean, nullable=False, default=True),
        sa.Column('super_user', sa.Boolean, nullable=False, default=False),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    op.drop_table('users')
