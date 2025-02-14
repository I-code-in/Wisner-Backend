"""002_add_product_images_and_ingredients

Revision ID: f28b96c0f996
Revises: aec020162b1d
Create Date: 2025-02-14 11:32:42.027618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision: str = 'f28b96c0f996'
down_revision: Union[str, None] = 'aec020162b1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('ingredients',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('energy_value', sa.String(), nullable=True),
                    sa.Column('portion', sa.String(), nullable=True),
                    sa.Column('amount_per_serving', sa.String(), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.Column('product_id', sa.BigInteger(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ["product_id"],
                        ["product.id"],
                    ),
                    sa.PrimaryKeyConstraint("id"),
                    )
    op.add_column('product', Column("image", String()))


def downgrade() -> None:
    op.drop_column('product', 'image')
    op.drop_table('ingredients')
