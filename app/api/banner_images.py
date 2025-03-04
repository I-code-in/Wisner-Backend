from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from app.crud.banner_images import (
    upload_banner_image, 
    get_active_banner_images, 
    deactivate_banner_image)
from app.database.database import get_db
from typing import Optional


router = APIRouter()


@router.post("/upload")
async def upload_banner_endpoint(
    file: UploadFile,
    name: Optional[str] = "",
    description: Optional[str] = "",
    db: Session = Depends(get_db)
):
    return await upload_banner_image(db, file, name, description)


@router.get("/active")
def get_active_banners_endpoint(db: Session = Depends(get_db)):
    return get_active_banner_images(db)


@router.put("/{banner_id}/deactivate")
def deactivate_banner_endpoint(banner_id: int, db: Session = Depends(get_db)):
    return deactivate_banner_image(db, banner_id)