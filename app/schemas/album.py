from pydantic import BaseModel
from datetime import datetime

class AlbumBase(BaseModel):
    nombre: str
    cantante_id: int
    precio: float
    genero: str

class AlbumCreate(AlbumBase):
    pass

class AlbumResponse(AlbumBase):
    id: int
    fecha_lanzamiento: datetime

class Config:
    orm_mode = True
