from sqlmodel import Field, SQLModel, Relationship
from typing import Optional


class UserBase(SQLModel):
    email: str
    password: str


class User(UserBase, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    active: bool
    super_user: bool
