from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks, Response
from app.models.newsletter import Newsletter
from app.schemas.newsletter import NewsletterCreate, NewsletterUpdate
from app.schemas.coupons import CouponsCreate, CouponsOut
from app.utils.email import send_email
from jinja2 import Environment, FileSystemLoader
from app.crud.coupons import new_coupons
from datetime import datetime, timedelta
from decouple import config as configEnv

env = Environment(loader=FileSystemLoader("app/templates/emails"))


def get_newsletter_all(db: Session, active: bool):
    result: list[Newsletter] = db.query(Newsletter).filter(Newsletter.active == active).all()
    return result


async def create_newsletter(db: Session, newsletter: NewsletterCreate, background_tasks: BackgroundTasks):
    result = db.query(Newsletter).filter(Newsletter.email == newsletter.email).first()
    if result and result.active is False:
        result.active = True
        template = env.get_template("resuscripcion.html")
        html_content = template.render()
        await send_email(
            [newsletter.email],
            "Resuscripción a Wisner Newsletter",
            html_content,
            background_tasks
        )
        return Response(content="Resuscripto a la Newsletter", status_code=200)
    elif result and result.active is True:
        raise HTTPException(status_code=404, detail="Email ya forma parte de la newsletter")
    else:
        result = Newsletter(**newsletter.model_dump())
        db.add(result)
    db.commit()
    db.refresh(result)

    template = env.get_template("suscripcion.html")
    cupon_create = CouponsCreate(
        email=result.email,
        discount=int(configEnv("DISCOUNT_CUPONS", "10")),
        generate=datetime.now(),
        expired=datetime.now() + timedelta(days=int(configEnv("DAYS_EXPIRE_CUPONS", "2"))),
        used=False
    )
    cupon: CouponsOut = new_coupons(db, cupon_create)
    html_content = template.render(cupon=cupon.uuid)
    await send_email(
        [newsletter.email],
        "Suscripción a Wisner Newsletter",
        html_content,
        background_tasks
    )

    return result


def update_newsletter(db: Session, update: NewsletterUpdate):
    old = db.query(Newsletter).filter(Newsletter.email == update.email).first()

    if not old:
        raise HTTPException(status_code=404, detail="No existe el email solicitado")

    update_data = update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(old, key, value)

    db.commit()
    db.refresh(old)

    return old