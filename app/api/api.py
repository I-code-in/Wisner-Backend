from fastapi import APIRouter
from app.api import products, pagos, coupons


api_router = APIRouter()

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