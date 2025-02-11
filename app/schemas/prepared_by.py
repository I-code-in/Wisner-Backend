from pydantic import BaseModel
from typing import Optional


class PreparedByBase(BaseModel):
    name: str
    ruc: str
    address: str
    city: str
    country: str
    phone: str
    email: str
    re: str
    rspa: str


class PreparedBy(PreparedByBase):
    id: int

    class Config:
        from_attributes = True