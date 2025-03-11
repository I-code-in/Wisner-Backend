from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    active: bool


class UserOut(UserBase):
    id: int


class UserIn(UserCreate):
    pass


class NewPassword(BaseModel):
    token: str
    new_password: str