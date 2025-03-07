from fastapi import BackgroundTasks, APIRouter
from app.models.contact import ContactBase
from app.utils.email import send_email
from jinja2 import Environment, FileSystemLoader
import os

router = APIRouter()

env = Environment(loader=FileSystemLoader("app/templates/emails"))


@router.post("/")
async def send_contact_email(form_data: ContactBase, background_tasks: BackgroundTasks):

    mail_receiver = os.getenv("MAIL_FROM")
    if not mail_receiver:
        return {"error": "MAIL_FROM no está configurado"}

    template = env.get_template("contactenos.html")

    html_content = template.render(
        nombre=form_data.nombre,
        email=form_data.email,
        telefono=form_data.telefono,
        mensaje=form_data.mensaje
    )

    await send_email(
        [mail_receiver], 
        "Nuevo mensaje de contacto",
        html_content,
        background_tasks
    )

    return {"message": "Email enviado correctamente"}