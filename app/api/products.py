from fastapi import APIRouter, UploadFile, File
from app.api.deps import CurrentSuperUser, SessionDep
from app.crud.products import (
    create_product,
    get_products_by_id,
    get_products_all,
    add_ingredients,
    create_prepare_by,
    update_ingredients,
    update_prepare_by,
    update_product,
    upload_image_product,
    get_ingredients
)
from app.schemas.products import Products, ProductsCreate, ProductsPaginate
from app.schemas.ingredients import IngredientsCreate, Ingredients
from app.schemas.prepared_by import PreparedBy, PreparedByCreate

router = APIRouter()


@router.post("", response_model=Products)
def api_create_product(product: ProductsCreate, db: SessionDep, current_user: CurrentSuperUser):
    return create_product(db, product)


@router.patch("/{product_id}", response_model=Products)
def api_edit_product(product_id: int, product: ProductsCreate, db: SessionDep, current_user: CurrentSuperUser):
    return update_product(db, product_id, product)


@router.get("", response_model=ProductsPaginate)
async def api_get_product_all(
    db: SessionDep,
    page: int = 1,
    limit: int = 8,
):
    return await get_products_all(db=db, page=page, limit=limit)


@router.get("/{id}", response_model=Products)
def api_get_product_by_id(id: int, db: SessionDep):
    return get_products_by_id(db, id)


@router.post("/product-upload-image/{product_id}")
async def api_upload_image_product(db: SessionDep, product_id: int, current_user: CurrentSuperUser, file: UploadFile = File(...)):
    return await upload_image_product(db, file, product_id)


@router.get("/ingredients/{product_id}", response_model=list[Ingredients])
def api_get_indgredients(product_id: int, db: SessionDep):
    return get_ingredients(db, product_id)


@router.post("/ingredients/{product_id}", response_model=list[Ingredients])
def api_add_indgredients(product_id: int, ingredients: list[IngredientsCreate], db: SessionDep, current_user: CurrentSuperUser):
    return add_ingredients(db, product_id, ingredients)


@router.patch("/ingredients/{ingredient_id}", response_model=Ingredients)
def api_edit_indgredients(ingredient_id: int, ingredients: IngredientsCreate, db: SessionDep, current_user: CurrentSuperUser):
    return update_ingredients(db, ingredient_id, ingredients)


@router.post("/prepared_by", response_model=PreparedBy)
def api_create_prepare_by(prepare_by: PreparedByCreate, db: SessionDep, current_user: CurrentSuperUser):
    return create_prepare_by(db, prepare_by)


@router.patch("/prepared_by/{prepared_by_id}", response_model=PreparedBy)
def api_edit_prepared_by(prepared_by_id: int, prepared_by: PreparedByCreate, db: SessionDep, current_user: CurrentSuperUser):
    return update_prepare_by(db, prepared_by_id, prepared_by)