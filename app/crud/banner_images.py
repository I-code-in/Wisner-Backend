from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile
import os
from uuid import uuid4
from pathlib import Path
import base64
from app.models.banner_images import BannerImage

BANNER_IMAGE_FOLDER= os.getenv("BANNER_IMAGE_FOLDER", "files/banner_image")
os.makedirs(BANNER_IMAGE_FOLDER, exist_ok=True)

async def upload_banner_image(db: Session, file:UploadFile, bannerImage_id: int):
    if file.content_type not in["image/jpeg", 'image/png']:
        raise HTTPException(status_code=400, detail="Solo se permiten imágenes en formato JPEG o PNG")
    
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid4()}.{file_extension}"
    file_path = os.path.join(BANNER_IMAGE_FOLDER, unique_filename)
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
        
    banner_image = BannerImage()
    banner_image.name = "01"
    banner_image.description = "hola"
    banner_image.dir = file_path
    banner_image.active = True
    
    db.add(banner_image)
    db.commit()
    
    return {"message": "Imagen subida exitosamente"}


def get_active_banner_images(db:Session):
    banner_images = db.query(BannerImage).filter(BannerImage.active == True).all()
    for img in banner_images:
        file_path = Path(img.dir)
        if file_path.is_file():
            try:
                with open(file_path, "rb") as image_file:
                    img.dir = base64.b64encode(image_file.read()).decode("utf-8")
            except Exception as e:
                print("Exception", e)
                img.dir = "Sin imagen"
                
        else:
            img.dir = "Sin imagen"    
            
    return banner_images


def deactivate_banner_image(db: Session, banner_id:int):
    banner_image = db.query(BannerImage).filter(BannerImage.id == banner_id).first()

    if not banner_image:
            raise HTTPException(status_code=404, detail="Imagen no encontrada")

    banner_image.active = False
    db.commit()
    db.refresh(banner_image)

    return {"message": "Imagen desactivada exitosamente"}