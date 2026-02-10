from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base

class Cantante(Base):
    __tablename__ = "cantantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, unique=True)
    edad = Column(Integer, nullable=False)
    genero_musical = Column(String, nullable=False)
    oyentes_mensuales_spotify = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    
