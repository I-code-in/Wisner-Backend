from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declarar las clases de los modelos
Base = declarative_base()

def get_db() -> Session:
    from app.database.database import SessionLocal  # Move the import inside to avoid circular issues
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()