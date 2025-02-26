from sqlmodel import Field, SQLModel


class NewsletterBase(SQLModel):
    email: str
    active: bool


class Newsletter(NewsletterBase, table=True):
    __tablename__ = "newsletter"
    id: int = Field(primary_key=True)