from fastapi import APIRouter
from app.api import (
    products,
    pagos,
    coupons,
    banner_images,
    newsletter,
    contact,
    user,
    login
)


api_router = APIRouter()

api_router.include_router(
    login.router,
    prefix="/login",
    tags=["login"]
)

api_router.include_router(
    user.router,
    prefix="/user",
    tags=["user"]
)

api_router.include_router(
    products.router,
    prefix="/products",
    tags=["products"]
)

api_router.include_router(
    pagos.router,
    prefix="/pedidos",
    tags=["pedidos"]
)

api_router.include_router(
    coupons.router,
    prefix="/coupons",
    tags=["coupons"]
)

api_router.include_router(
    banner_images.router,
    prefix="/banner_images",
    tags=["banner_images"]
)

api_router.include_router(
    newsletter.router,
    prefix="/newsletter",
    tags=["newsletter"]
)

api_router.include_router(
    contact.router,
    prefix="/contact",
    tags=["contact"]
)