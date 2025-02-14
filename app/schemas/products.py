from pydantic import BaseModel
from typing import Optional
from app.schemas.prepared_by import PreparedBy


class ProductsBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None
    description: Optional[str] = None
    warning: Optional[str] = None
    active: Optional[bool] = None
    prepared_by_id: Optional[int] = None


class ProductsCreate(ProductsBase):
    pass

    class Config:
        from_attributes = True 


class Products(ProductsBase):
    image: Optional[str]
    prepared_by: Optional[PreparedBy]

    class Config:
        from_attributes = True


class ProductsPaginate(BaseModel):
    total: int
    page: int
    limit: int
    totalPage: int
    items: list[Products]