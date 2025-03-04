from pydantic import BaseModel
from typing import Optional


class Productos(BaseModel):
    cantidad: int
    product_id: int


class Order(BaseModel):
    ruc: Optional[str] = ""
    email: Optional[str] = ""
    nombre: str
    telefono: str
    direccion: Optional[str] = ""
    documento: str
    razon_social: Optional[str] = ""
    productos: list[Productos]


class OrderIn(Order):
    pass
