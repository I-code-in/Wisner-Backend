from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.coupons import Coupons
from app.schemas.coupons import CouponsOut, CouponsCreate, CouponsUpdate, CouponsPaginate
import re


def get_coupons_by_uuid(db: Session, uuid: str, email: str) -> CouponsOut:
    result = db.query(Coupons).filter(Coupons.uuid == uuid).first()

    if not result:
        raise HTTPException(404, detail="No existe el cupon solicitado")

    if not result.active:
        raise HTTPException(400, detail="El cupon solicitado ya no esta activo")

    if result.used:
        raise HTTPException(400, detail="El cupon solicitado ya fue usado")

    if result.email != "" and result.email != email:
        raise HTTPException(400, detail="El cupon no pertenece al email asociado")

    if result.expired <= datetime.now():
        raise HTTPException(400, detail="El cupon ya expiro")

    return CouponsOut(**result.model_dump())


def new_coupons(db: Session, coupons: CouponsCreate) -> CouponsOut:
    new_cupon = Coupons(**coupons.model_dump())
    new_cupon.generate = datetime.now()

    if new_cupon.generate >= new_cupon.expired:
        raise HTTPException(400, detail="La fecha de vencimiento no puede ser menor que la fecha actual")

    if new_cupon.discount >= 100 or new_cupon.discount < 0:
        raise HTTPException(400, detail="El descuento no puede ser igual o mayor a 100 por ciento o menor a 0 por ciento")

    if new_cupon.email and not re.match(r"[^@]+@[^@]+\.[^@]+", new_cupon.email):
        raise HTTPException(400, detail="Email no valido")
    
    db.add(new_cupon)
    db.commit()
    db.refresh(new_cupon)

    return CouponsOut(**new_cupon.model_dump())


def update_coupons(db: Session, coupons: CouponsUpdate, uuid: str):
    cupon = db.query(Coupons).filter(Coupons.uuid == uuid).first()

    if not cupon:
        raise HTTPException(status_code=404, detail="No existe el cupon solicitado")

    update_data = coupons.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cupon, key, value)

    if cupon.generate >= cupon.expired:
        raise HTTPException(400, detail="La fecha de vencimiento no puede ser menor que la fecha actual")

    if cupon.discount >= 100 or cupon.discount < 0:
        raise HTTPException(400, detail="El descuento no puede ser igual o mayor a 100 por ciento o menor a 0 por ciento")

    if cupon.email and not re.match(r"[^@]+@[^@]+\.[^@]+", cupon.email):
        raise HTTPException(400, detail="Email no valido")

    db.commit()
    db.refresh(cupon)

    return CouponsOut(**cupon.model_dump())


def get_cupons_all(db: Session, used: bool, active: bool, email: str, page: int = 1, limit: int = 8) -> CouponsPaginate:
    query = db.query(Coupons)
    total_items = query.count()
    total_pages = (total_items + limit - 1) // limit
    skip = (page - 1) * limit
    if used:
        query.filter(Coupons.used == used)
    if active:
        query.filter(Coupons.active == active)
    if email:
        query.filter(Coupons.email.like(f"%{email}%"))
    items = query.order_by(Coupons.id.asc()).offset(skip).limit(limit).all()

    return CouponsPaginate(
        total=total_items,
        page=page,
        limit=limit,
        totalPage=total_pages,
        items=items
    )