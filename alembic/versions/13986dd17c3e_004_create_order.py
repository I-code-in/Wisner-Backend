"""004_create_order

Revision ID: 13986dd17c3e
Revises: 5f3e21815bf3
Create Date: 2025-02-21 11:11:06.856191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '13986dd17c3e'
down_revision: Union[str, None] = '5f3e21815bf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'comprador',
        sa.Column('id', sa.BigInteger, nullable=False),
        sa.Column('ruc', sa.String, nullable=True, default=""),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('ciudad', sa.Integer, nullable=False, default=1),
        sa.Column('nombre', sa.String, nullable=False),
        sa.Column('telefono', sa.String, nullable=False),
        sa.Column('direccion', sa.String, nullable=True, default=""),
        sa.Column('documento', sa.String, nullable=False),
        sa.Column('coordenadas', sa.String, nullable=True, default=""),
        sa.Column('razon_social', sa.String, nullable=True, default=""),
        sa.Column('tipo_documento', sa.String, nullable=False, default="CI"),
        sa.Column('direccion_referencia', sa.String, nullable=True, default=""),
        sa.PrimaryKeyConstraint("id")                 
    )
    op.create_table(
        'coupons',
        sa.Column('id', sa.BigInteger, nullable=False),
        sa.Column('uuid', UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False),
        sa.Column('email', sa.String, nullable=True),
        sa.Column('discount', sa.Integer, nullable=True),
        sa.Column('generate', sa.DateTime, nullable=False),
        sa.Column('expired', sa.DateTime, nullable=False),
        sa.Column('used', sa.Boolean, nullable=False, default=False),
        sa.Column('active', sa.Boolean, nullable=False, default=True),
        sa.PrimaryKeyConstraint("id")             
    )
    op.create_table(
        'pedido',
        sa.Column('id', sa.BigInteger, nullable=False),
        sa.Column('token', sa.String, nullable=False),
        sa.Column('public_key', sa.String, nullable=False),
        sa.Column('coupons_id', sa.BigInteger, nullable=True),
        sa.Column('sub_monto', sa.BigInteger, nullable=False),
        sa.Column('monto_total', sa.BigInteger, nullable=False),
        sa.Column('tipo_pedido', sa.String, nullable=False, default="VENTA-COMERCIO"),
        sa.Column('comprador_id', sa.BigInteger, nullable=False),
        sa.Column('fecha_maxima_pago', sa.DateTime, nullable=False),
        sa.Column('id_pedido_comercio', sa.BigInteger, nullable=False),
        sa.Column('descripcion_resumen', sa.String, nullable=False, default=""),
        sa.Column('forma_pago', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["coupons_id"],
            ["coupons.id"]
        ),
        sa.ForeignKeyConstraint(
            ["comprador_id"],
            ["comprador.id"]
        ),
    )
    op.create_table(
        'compras_items',
        sa.Column('id', sa.BigInteger, nullable=False),
        sa.Column('pedido_id', sa.BigInteger, nullable=False),
        sa.Column('coupons_id', sa.BigInteger, nullable=False),
        sa.Column('ciudad', sa.String, nullable=True, default="1"),
        sa.Column('nombre', sa.String, nullable=False),
        sa.Column('cantidad', sa.Integer, nullable=False),
        sa.Column('categoria', sa.String, nullable=True, default="909"),
        sa.Column('public_key', sa.String, nullable=False),
        sa.Column('url_imagen', sa.String, nullable=True, default=""),
        sa.Column('descripcion', sa.String, nullable=False),
        sa.Column('id_producto', sa.BigInteger, nullable=False),
        sa.Column('precio_unitario', sa.Integer, nullable=False),
        sa.Column('sub_total', sa.BigInteger, nullable=False),
        sa.Column('precio_total', sa.BigInteger, nullable=False),
        sa.Column('vendedor_telefono', sa.String, nullable=True, default=""),
        sa.Column('vendedor_direccion', sa.String, nullable=True, default=""),
        sa.Column('vendedor_direccion_referencia', sa.String, nullable=True, default=""),
        sa.Column('vendedor_direccion_coordenadas', sa.String, nullable=True, default=""),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["pedido_id"],
            ["pedido.id"]
        ),
        sa.ForeignKeyConstraint(
            ["coupons_id"],
            ["coupons.id"]
        ),
        sa.ForeignKeyConstraint(
            ["id_producto"],
            ["product.id"]
        ),
    )
    op.create_table(
        'newsletter',
        sa.Column('id', sa.BigInteger, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('active', sa.Boolean, nullable=False),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    op.drop_table('newsletter')
    op.drop_table('compras_items')
    op.drop_table('pedido')
    op.drop_table('coupons')
    op.drop_table('comprador')
