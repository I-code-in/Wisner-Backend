from sqlmodel import Field, SQLModel
from datetime import datetime, timedelta
from uuid import UUID, uuid4
from typing import Optional


class CouponsBase(SQLModel):   
    email: str
    discount: int
    generate: datetime = Field(default_factory=datetime.now)
    expired: datetime = Field(default_factory=lambda: datetime.now() + timedelta(days=2))
    used: bool


class Coupons(CouponsBase, table=True):
    __tablename__ = "coupons"
    id: Optional[int] = Field(default=None, primary_key=True)
    active: bool = True
    uuid: UUID = Field(default_factory=uuid4)