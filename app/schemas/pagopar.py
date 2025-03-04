from typing import List
from datetime import datetime
from pydantic import BaseModel


class Comprador(BaseModel):
    ruc: str
    email: str
    ciudad: str
    nombre: str
    telefono: str
    direccion: str
    documento: int
    coordenadas: str
    razon_social: str
    tipo_documento: str
    direccion_referencia: str


class ComprasItem(BaseModel):
    ciudad: int
    nombre: str
    cantidad: int
    categoria: int
    public_key: str
    url_imagen: str
    descripcion: str
    id_producto: int
    precio_total: int
    vendedor_telefono: str
    vendedor_direccion: str
    vendedor_direccion_referencia: str
    vendedor_direccion_coordenadas: str


class Transaccion(BaseModel):
    token: str
    comprador: Comprador
    public_key: str
    monto_total: int
    tipo_pedido: str
    compras_items: List[ComprasItem]
    fecha_maxima_pago: datetime
    id_pedido_comercio: str
    descripcion_resumen: str
    forma_pago: int