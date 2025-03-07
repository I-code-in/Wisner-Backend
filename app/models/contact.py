from pydantic import BaseModel


class ContactBase(BaseModel):
    nombre: str
    email: str
    telefono: str
    mensaje: str
