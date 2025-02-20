"""001_create_products

Revision ID: a1ca59841855
Revises: e7877a75c5ea
Create Date: 2025-02-14 16:40:38.671071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1ca59841855'
down_revision: Union[str, None] = 'e7877a75c5ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
