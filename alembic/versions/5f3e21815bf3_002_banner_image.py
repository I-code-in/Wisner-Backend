"""002_banner_image

Revision ID: 5f3e21815bf3
Revises: a1ca59841855
Create Date: 2025-02-19 16:33:26.843681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f3e21815bf3'
down_revision: Union[str, None] = 'f28b96c0f996'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table("banner_image",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("dir", sa.String(), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id")
     )
 


def downgrade() -> None:
    pass
