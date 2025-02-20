from pydantic import BaseModel
from typing import Optional


class IngredientsBase(BaseModel):
    energy_value: Optional[str] = None
    portion: Optional[str] = None
    amount_per_serving: Optional[str] = None
    active: Optional[bool] = None


class IngredientsCreate(IngredientsBase):
    pass


class IngredientsUpdate(IngredientsBase):
    active: bool


class Ingredients(IngredientsBase):
    id: int
    product_id: int
    active: bool

    class Config:
        from_attributes = True