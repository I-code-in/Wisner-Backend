from pydantic import BaseModel
from typing import Optional

class BannerImageBase(BaseModel):
    name:str
    description: str
    dir: str
    active: bool
    
class BannerImageCreate(BannerImageBase):
    pass

class BannerImage(BannerImageBase):
    id: int
    class Config:
        from_attributes = True

