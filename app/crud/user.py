from fastapi import APIRouter, Depends, HTTPException, Response
from app.core.security import get_password_hash, verify_password, create_access_token
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserOut, UserIn
from app.schemas.token import Token
from datetime import timedelta
from decouple import config as env


def user_create(user: UserCreate, db: Session):
    user_exists = db.query(User).filter(User.email == user.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    password = get_password_hash(user.password)
    new_user = User(
        email=user.email,
        password=password,
        active=True,
        super_user=False
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token_expires = timedelta(minutes=int(env("ACCESS_TOKEN_EXPIRE_MINUTES"), 30))

    return Token(
        access_token=create_access_token(
            new_user.id, expires_delta=access_token_expires
        )
    )


def get_by_email(email: str, db: Session):
    user_exists = db.query(User).filter(User.email == email).first()

    if not user_exists:
        raise HTTPException(status_code=400, detail="Email no existe")

    if not user_exists.active:
        raise HTTPException(status_code=400, detail="Usuario inactivo")

    return user_exists


def authenticate(user: UserIn, db: Session):
    user_exists = db.query(User).filter(User.email == user.email).first()

    if not user_exists:
        raise HTTPException(status_code=404, detail="Usuario o contraseña incorrecto")

    if not verify_password(user.password, user_exists.password):
        raise HTTPException(status_code=404, detail="Usuario o contraseña incorrecto")

    if not user_exists.active:
        raise HTTPException(status_code=404, detail="Usuario inactivo")

    return user_exists