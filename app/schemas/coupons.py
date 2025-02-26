from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, timedelta
from typing import Optional


class CouponsBase(BaseModel):
    email: Optional[str] = ""
    discount: Optional[int] = 10
    generate: Optional[datetime] = datetime.now()
    expired: Optional[datetime] = datetime.now() + timedelta(days=2)
    used: Optional[bool] = False
    active: Optional[bool] = True


class Coupons(CouponsBase):
    id: Optional[int] = None
    uuid: Optional[UUID] = None

    class Config:
        from_attributes = True


class CouponsOut(BaseModel):
    uuid: UUID
    discount: int
    expired: datetime


class CouponsCreate(CouponsBase):
    pass


class CouponsUpdate(CouponsCreate):
    pass


class CouponsPaginate(BaseModel):
    total: int
    page: int
    limit: int
    totalPage: int
    items: list[Coupons]