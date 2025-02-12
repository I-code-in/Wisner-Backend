from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api

app = FastAPI()

origins = [
    "http://localhost:4200",  # URL de tu frontend Angular
    "http://127.0.0.1:4200"  # Otra posible URL de desarrollo
]


@app.on_event("startup")
async def startup():
    pass

app.include_router(api.api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Orígenes permitidos
    allow_credentials=True,  # Permitir cookies/envío de credenciales
    allow_methods=["*"],  # Métodos HTTP permitidos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Encabezados permitidos
)