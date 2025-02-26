from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks, Response
from app.models.newsletter import Newsletter
from app.schemas.newsletter import NewsletterCreate, NewsletterUpdate
from app.utils.email import send_email
from jinja2 import Environment, FileSystemLoader

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
        result = Newsletter(**newsletter)
        db.add(result)
    db.commit()
    db.refresh(result)

    template = env.get_template("resuscripcion.html")
    html_content = template.render()
    await send_email(
        [newsletter.email],
        "Resuscripción a Wisner Newsletter",
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