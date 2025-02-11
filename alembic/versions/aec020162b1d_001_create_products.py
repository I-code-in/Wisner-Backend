"""001_create_products

Revision ID: aec020162b1d
Revises: 
Create Date: 2025-02-11 17:08:43.990797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aec020162b1d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('prepared_by',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('ruc', sa.String(), nullable=True),
                    sa.Column('address', sa.String(), nullable=True),
                    sa.Column('city', sa.String(), nullable=True),
                    sa.Column('country', sa.String(), nullable=True),
                    sa.Column('phone', sa.String(), nullable=True),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('re', sa.String(), nullable=True),
                    sa.Column('rspa', sa.String(), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint("id"),
                    )
    op.execute("""
        insert into prepared_by (name, ruc, address, city, country, email, phone, re, rspa, active) values
               (\'Laura Gabriela Gali Sosa\', \'3492443-4\', \'Manuel Ortiz Guerrero c/ Av. San Antonio N° 176\', \'San Antonio\', \'Paraguay\', \'+595986799774\', \'wisnerchocolate@gmail.com\', '34924434/1', '', True)
    """)
    op.execute("""
        insert into prepared_by (name, ruc, address, city, country, email, phone, re, rspa, active) values
               (\'Laura Gabriela Gali Sosa\', \'3492443-4\', \'Manuel Ortiz Guerrero c/ Av. San Antonio N° 176\', \'San Antonio\', \'Paraguay\', \'+595986799774\', \'wisnerchocolate@gmail.com\', '34924434/1', '87916', True)
    """)
    op.create_table('product',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('value', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('warning', sa.String(), nullable=True),
                    sa.Column('prepared_by_id', sa.BigInteger(), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ["prepared_by_id"],
                        ["prepared_by.id"],
                    ),
                    sa.PrimaryKeyConstraint("id"),
                    )

    op.execute("""
        insert into product (name, value, description, warning, prepared_by_id, active) values
               (\'Wisner Chocolate con leche\', 35000, \'Azúcar, manteca de cacao, leche entera, masa de cacao, leche descremada, emulsionante: lecitina de soja, aromatizante: esencia de vainilla.\', \'Contiene leche y derivado de soja\', 2, True)
    """)
    op.execute("""
        insert into product (name, value, description, warning, prepared_by_id, active) values
               (\'Wisner Chocolate sin azúcar\', 35000, \'Masa de cacao, maltitol, manteca de cacao, emulsionante: lecitina de soja, aromatizante: esencia de vainilla.\', \'Contiene derivado de soja\', 1, True)
    """)
    op.execute("""
        insert into product (name, value, description, warning, prepared_by_id, active) values
               (\'Wisner Chocolate\', 35000, \'Masa de cacao, azúcar orgánica, manteca de cacao, emulsionante: lecitina de soja, aromatizante: esencia de vainilla.\', \'Contiene derivado de soja\', 2, True)
    """)


def downgrade() -> None:
    op.drop_table('product')
    op.drop_table('prepared_by')
