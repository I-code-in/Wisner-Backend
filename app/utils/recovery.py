from fastapi import BackgroundTasks
from app.utils.email import send_email
from decouple import config as env
from jinja2 import Environment, FileSystemLoader

templates = Environment(loader=FileSystemLoader("app/templates/emails"))


async def send_reset_password_email(email_to: str, token: str, background_tasks: BackgroundTasks) -> None:

    template = templates.get_template("reset_password.html")
    server_host = str(env("FRONTEND", "localhost:4200"))
    link = f"{server_host}/reset-password?token={token}"
    html_content = template.render(link=link, email=email_to)
    await send_email(
        [email_to],
        "Wisner - Recuperación de contraseña",
        html_content,
        background_tasks
    )