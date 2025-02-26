from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, UploadFile 
from fastapi.responses import JSONResponse
import base64
from pathlib import Path
from app.models.products import Product
from app.models.prepared_by import PreparedBy
from app.models.ingredients import Ingredients
from app.schemas.products import ProductsCreate, ProductsPaginate
from app.schemas.ingredients import IngredientsCreate, IngredientsUpdate
from app.schemas.prepared_by import PreparedByCreate
import os
from uuid import uuid4

PRODUCT_IMAGEN_FOLDER = os.getenv("PRODUCT_IMAGEN_FOLDER", "files/product_images")
os.makedirs(PRODUCT_IMAGEN_FOLDER, exist_ok=True)


def get_products_by_id(db: Session, id: int):
    return db.query(Product).options(joinedload(Product.prepared_by)).filter(Product.id == id).first()


async def get_products_all(db: Session, page: int = 1, limit: int = 8):
    query = db.query(Product).filter(Product.active == True)
    total_items = query.count()
    total_pages = (total_items + limit - 1) // limit
    skip = (page - 1) * limit
    items = query.order_by(Product.id.asc()).offset(skip).limit(limit).all()
    for record in items:
        if record.image is None:
            record.image = "Sin imagen"
            continue
        file_path = Path(record.image)
        if file_path.is_file():
            try:
                with open(file_path, "rb") as image_file:
                    record.image = base64.b64encode(image_file.read()).decode("utf-8")
            except Exception as e:
                print("Exception ", e)
                record.image = "Sin imagen"
        else:
            record.image = "Sin imagen"

    return ProductsPaginate(
        total=total_items,
        page=page,
        limit=limit,
        totalPage=total_pages,
        items=items
    )


def create_product(db: Session, product: ProductsCreate):
    product_add = Product(**product.dict())
    db.add(product_add)
    db.commit()
    db.refresh(product_add)
    return product_add


def get_ingredients(db: Session, product_id):
    return db.query(Ingredients).filter(Ingredients.product_id == product_id, Ingredients.active == True).all()


def add_ingredients(db: Session, product_id, ingredients: list[IngredientsCreate]):
    for record in ingredients:
        ingredients_add = Ingredients(**record.dict())
        ingredients_add.product_id = product_id
        ingredients_add.active = True
        db.add(ingredients_add)
    db.commit()
    return db.query(Ingredients).filter(Ingredients.product_id==product_id).all()


def create_prepare_by(db: Session, prepare_by: PreparedByCreate):
    prepare_by_add = PreparedBy(**prepare_by.dict())
    db.add(prepare_by_add)
    db.commit()
    db.refresh(prepare_by_add)
    return prepare_by_add


def update_product(db: Session, product_id, product: ProductsCreate):
    old = db.query(Product).filter(Product.id == product_id).first()
    if not old:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    try:
        for key, value in product.dict(exclude_unset=True).items():
            setattr(old, key, value)

        db.commit()
        db.refresh(old)
        return old
    except Exception as e:
        
        raise HTTPException(status_code=404, detail="Update faild: " + str(e))


def update_prepare_by(db: Session, prepare_by_id, prepare_by: PreparedByCreate):
    old = db.query(PreparedBy).filter(PreparedBy.id == prepare_by_id).first()
    if not old:
        raise HTTPException(status_code=404, detail="Ingredient not found")

    for key, value in prepare_by.dict(exclude_unset=True).items():
        setattr(old, key, value)

    db.commit()
    db.refresh(old)
    return old


def update_ingredients(db: Session, ingredient_id, ingredients: IngredientsUpdate):
    old = db.query(Ingredients).filter(Ingredients.id == ingredient_id).first()
    if not old:
        raise HTTPException(status_code=404, detail="Ingredient not found")

    for key, value in ingredients.dict(exclude_unset=True).items():
        setattr(old, key, value)

    db.commit()
    db.refresh(old)
    return old


async def upload_image_product(db: Session, file: UploadFile, product_id: int):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Solo se permiten imágenes en formato JPEG o PNG")
    
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid4()}.{file_extension}"
    file_path = os.path.join(PRODUCT_IMAGEN_FOLDER, unique_filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    product = db.query(Product).filter(Product.id == product_id).first()
    product.image = file_path

    db.commit()

    return {"message": "Imagen subida exitosamente"}