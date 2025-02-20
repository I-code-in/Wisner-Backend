"""001_create_products

Revision ID: e7877a75c5ea
Revises: aec020162b1d
Create Date: 2025-02-14 14:05:08.547292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7877a75c5ea'
down_revision: Union[str, None] = 'aec020162b1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
