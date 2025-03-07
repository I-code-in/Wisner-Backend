from datetime import datetime, timedelta
from typing import Any, Union, Optional

from jose import jwt
from passlib.context import CryptContext
from decouple import config as env

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: Union[timedelta, None] = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=int(env("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, str(env("SECRET_KEY", "")), algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, password: str) -> bool:
    return pwd_context.verify(plain_password, password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=int(env("EMAIL_RESET_TOKEN_EXPIRE_HOURS", 1)))
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email},
        str(env("SECRET_KEY", "")),
        algorithm=ALGORITHM,
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, str(env("SECRET_KEY", "")), algorithms=[ALGORITHM])
        return decoded_token["sub"]
    except jwt.JWTError:
        return None
