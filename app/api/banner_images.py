from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from app.crud.banner_images import (
    upload_banner_image, 
    get_active_banner_images, 
    deactivate_banner_image)
from app.database.database import get_db


router = APIRouter(
)

        
@router.post("/upload/{bannerImage_id}")
async def upload_banner_endpoint(
    bannerImage_id: int, 
    file: UploadFile, 
    db: Session = Depends(get_db)
):
    return await upload_banner_image(db, file, bannerImage_id)        

@router.get("/active")
def get_active_banners_endpoint(db: Session = Depends(get_db)):
    return get_active_banner_images(db)


@router.put("/{banner_id}/deactivate")
def deactivate_banner_endpoint(banner_id: int, db: Session = Depends(get_db)):
    return deactivate_banner_image(db, banner_id)    