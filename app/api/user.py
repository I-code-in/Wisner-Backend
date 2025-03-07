from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.schemas.user import UserBase, UserCreate, UserUpdate, UserOut, UserIn
from app.schemas.token import Token
from app.crud.user import user_create, authenticate
from app.core.security import create_access_token
from typing import Optional
from app.database.database import get_db
from decouple import config as env
from datetime import timedelta

router = APIRouter()


@router.post("/register")
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user_create(user=user_data, db=db)
