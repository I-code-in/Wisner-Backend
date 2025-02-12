from pydantic import BaseModel
from typing import Optional
from app.schemas.prepared_by import PreparedBy


class ProductsBase(BaseModel):
    name: str
    value: int
    description: str
    warning: str
    active: bool
    prepared_by_id: int


class ProductsCreate(ProductsBase):
    pass


class Products(ProductsBase):
    id: int
    prepared_by: Optional[PreparedBy]

    class Config:
        from_attributes = True


class ProductsPaginate(BaseModel):
    total: int
    page: int
    limit: int
    totalPage: int
    items: list[Products]