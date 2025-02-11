from sqlalchemy.orm import Session, joinedload
from app.models.products import Product
from app.schemas.products import ProductsCreate


def get_products_by_id(db: Session, id: int):
    return db.query(Product).options(joinedload(Product.prepared_by)).filter(Product.id == id).first()


def get_products_all(db: Session, id: int):
    return db.query(Product).all()


def create_product(db: Session, product: ProductsCreate):
    product_add = Product(**product.dict())
    db.add(product_add)
    db.commit()
    db.refresh(product_add)
    return product_add