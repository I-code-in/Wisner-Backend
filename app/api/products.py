from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.crud.products import create_product, get_products_by_id, get_products_all
from app.schemas.products import Products, ProductsCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Products)
def api_create_product(product: ProductsCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@router.get("/", response_model=Products)
def api_get_product_all(db: Session = Depends(get_db)):
    return get_products_all(db)


@router.get("/{id}", response_model=Products)
def api_get_product_by_id(id: int, db: Session = Depends(get_db)):
    return get_products_by_id(db, id)