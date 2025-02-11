from sqlmodel import Field, SQLModel, Relationship
from typing import List


class PreparedByBase(SQLModel):
    name: str
    ruc: str
    address: str
    city: str
    country: str
    phone: str
    email: str
    re: str
    rspa: str


class PreparedBy(PreparedByBase, table=True):
    __tablename__ = "prepared_by"
    id: int = Field(primary_key=True)
    active: bool
    product: List["Product"] = Relationship(back_populates="prepared_by")