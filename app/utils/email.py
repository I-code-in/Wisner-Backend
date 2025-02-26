from fastapi import BackgroundTasks
from fastapi_mail import FastMail, ConnectionConfig, MessageSchema
from decouple import config as env

conf = ConnectionConfig(
    MAIL_USERNAME=str(env("MAIL_USERNAME", "")),
    MAIL_PASSWORD=str(env("MAIL_PASSWORD", "")),
    MAIL_FROM=str(env("MAIL_FROM", "")),
    MAIL_PORT=env("MAIL_PORT", ""),
    MAIL_SERVER=str(env("MAIL_SERVER", "")),
    MAIL_STARTTLS=env("MAIL_STARTTLS", ""),
    MAIL_SSL_TLS=env("MAIL_SSL_TLS", ""),
    USE_CREDENTIALS=env("USE_CREDENTIALS", "")
)


async def send_email(
    email_recipients: list[str],
    subject: str,
    body: str,
    background_tasks: BackgroundTasks
):
    message = MessageSchema(
        subject=subject,
        recipients=email_recipients,
        body=body,
        subtype="html",
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Email enviado con éxito"}