from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Leer la URL de la base de datos desde variable de entorno
# Si no existe, usar SQLite por defecto (para desarrollo local sin Docker)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database/database.db")

# Configuración específica para SQLite
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()