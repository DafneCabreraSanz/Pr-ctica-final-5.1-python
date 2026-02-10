from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from database.database import Base
from datetime import datetime

class Album(Base):
    __tablename__ = "albumes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, unique=True)
    cantante_id = Column(Integer, ForeignKey("cantantes.id"), nullable=False)
    precio = Column(Float, nullable=False)
    fecha_lanzamiento = Column(DateTime, default=datetime.utcnow, nullable=False)
    genero = Column(String, nullable=False)
