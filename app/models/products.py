from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from app.models.prepared_by import PreparedBy


class ProductBase(SQLModel):
    name: str
    value: int
    description: str
    warning: str
    image: str


class Product(ProductBase, table=True):
    __tablename__ = "product"
    id: int = Field(primary_key=True)
    active: bool
    prepared_by_id: int = Field(
        default=None, foreign_key="prepared_by.id", nullable=False
    )
    prepared_by: Optional[PreparedBy] = Relationship(back_populates="product")
