from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserIn, NewPassword
from app.schemas.token import Token
from app.crud.user import authenticate, get_by_email
from app.core.security import (
    create_access_token,
    generate_password_reset_token,
    verify_password_reset_token,
    get_password_hash
)
from typing import Annotated
from app.api.deps import CurrentUser, SessionDep
from decouple import config as env
from datetime import timedelta
from app.utils.recovery import send_reset_password_email

router = APIRouter()

@router.post("")
def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep
) -> Token:
    user = authenticate(
        UserIn(email=form_data.username, password=form_data.password),
        session
    )

    access_token_expires = timedelta(minutes=int(env("ACCESS_TOKEN_EXPIRE_MINUTES"), 30))

    return Token(
        access_token=create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )


@router.post("/test-token")
def test_token(current_user: CurrentUser):
    """
    Test access token
    """
    return current_user


@router.post("/password-recovery/{email}")
async def recover_password(
    email: str,
    background_tasks: BackgroundTasks,
    session: SessionDep
):
    """
    Password Recovery
    """
    user = get_by_email(db=session, email=email)

    password_reset_token = generate_password_reset_token(email=email)
    await send_reset_password_email(
        email_to=user.email,
        token=password_reset_token,
        background_tasks=background_tasks
    )
    return {"message": "Password recovery email sent"}


@router.post("/reset-password")
def reset_password(
    body: NewPassword,
    session: SessionDep
):
    """
    Reset password
    """
    email = verify_password_reset_token(token=body.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")

    user = get_by_email(db=session, email=email)

    password = get_password_hash(password=body.new_password)
    user.password = password
    session.add(user)
    session.commit()
    return {"message": "Password updated successfully"}