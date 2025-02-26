from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.schemas.newsletter import NewsletterOut, NewsletterCreate, NewsletterUpdate
from app.crud.newsletter import get_newsletter_all, create_newsletter, update_newsletter
from typing import Optional
from app.database.database import get_db

router = APIRouter()

@router.post("/", response_model=NewsletterOut)
async def api_create_newslettert(background_tasks: BackgroundTasks, newsletter: NewsletterCreate, db: Session = Depends(get_db)):
    return await create_newsletter(db, newsletter, background_tasks)


@router.patch("/", response_model=NewsletterOut)
def api_update_newsletter(newsletter: NewsletterUpdate, db: Session = Depends(get_db)):
    return update_newsletter(db, newsletter)

@router.get("/", response_model=NewsletterOut)
def api_get_newsletter_all(active: bool, db: Session = Depends(get_db)):
    return get_newsletter_all(db, active)