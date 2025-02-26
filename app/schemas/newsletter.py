from pydantic import BaseModel
from typing import Optional


class NewsletterBase(BaseModel):
    email: str
    active: Optional[bool] = True


class NewsletterOut(NewsletterBase):
    pass


class NewsletterCreate(NewsletterBase):
    pass


class NewsletterUpdate(NewsletterBase):
    pass