from sqlmodel import Field, SQLModel


class IngredientsBase(SQLModel):
    energy_value: str
    portion: str
    amount_per_serving: str
    product_id: int


class Ingredients(IngredientsBase, table=True):
    __tablename__ = "ingredients"
    id: int = Field(primary_key=True)
    active: bool