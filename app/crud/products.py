from sqlalchemy.orm import Session, joinedload
from app.models.products import Product
from app.schemas.products import ProductsCreate, ProductsPaginate


def get_products_by_id(db: Session, id: int):
    return db.query(Product).options(joinedload(Product.prepared_by)).filter(Product.id == id).first()


def get_products_all(db: Session, page: int = 0, limit: int = 8):
    query = db.query(Product)
    total_items = query.count()
    total_pages = (total_items + limit - 1) // limit
    skip = (page - 1) * limit
    items = query.offset(skip).limit(limit).all()
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