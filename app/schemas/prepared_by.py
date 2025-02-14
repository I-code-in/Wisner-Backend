from pydantic import BaseModel
from typing import Optional


class PreparedByBase(BaseModel):
    name: Optional[str] = None
    ruc: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    re: Optional[str] = None
    rspa: Optional[str] = None
    active: Optional[bool] = None


class PreparedBy(PreparedByBase):
    id: int

    class Config:
        from_attributes = True


class PreparedByCreate(PreparedByBase):
    pass