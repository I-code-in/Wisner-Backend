from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.coupons import CouponsOut, CouponsCreate, CouponsUpdate, CouponsPaginate
from app.crud.coupons import get_coupons_by_uuid, new_coupons, update_coupons, get_cupons_all
from typing import Optional

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{cupon}", response_model=CouponsOut)
def api_get_coupons_by_uuid(cupon: str, email: Optional[str] = "", db: Session = Depends(get_db)):
    return get_coupons_by_uuid(db, cupon, email)


@router.post("", response_model=CouponsOut)
def api_new_coupons(cupon: CouponsCreate, db: Session = Depends(get_db)):
    return new_coupons(db, cupon)


@router.patch("/{cupon}", response_model=CouponsOut)
def api_edit_coupons(cupon: str, cuponUpdate: CouponsUpdate, db: Session = Depends(get_db)):
    return update_coupons(db, cuponUpdate, cupon)


@router.get("", response_model=CouponsPaginate)
def api_get_coupons(
        used: Optional[bool] = None,
        active: Optional[bool] = None,
        email: Optional[str] = None,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        db: Session = Depends(get_db)
    ):
    return get_cupons_all(
        used=used,
        db=db,
        active=active,
        email=email,
        page=page,
        limit=limit
    )