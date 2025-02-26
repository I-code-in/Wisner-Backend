from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.orders import OrderIn
from app.utils.email import send_email

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/solicitar-pedido", response_model=None)
async def api_iniciar_transaccion(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    return await send_email(["vrcogliolo@gmail.com"], "Prueba de correo", "<h2>¡Hola!</h2><p>Este es un correo de prueba.</p>", background_tasks)