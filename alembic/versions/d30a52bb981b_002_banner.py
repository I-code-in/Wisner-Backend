"""002_banner

Revision ID: d30a52bb981b
Revises: 5f3e21815bf3
Create Date: 2025-02-20 21:44:55.569402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd30a52bb981b'
down_revision: Union[str, None] = '5f3e21815bf3'
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
    pass


def downgrade() -> None:
    pass
