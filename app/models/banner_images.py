from sqlmodel import Field, SQLModel
from typing import Optional

    
class BannerImageBase(SQLModel):
    name: str
    description: str
    dir: str
    
class BannerImage(BannerImageBase, table=True):
    __tablename__= "banner_image"
    id: int = Field(primary_key=True)
    active: bool
    
