from pydantic import BaseModel

class CantanteBase(BaseModel):
    nombre: str
    edad: int
    genero_musical: str
    oyentes_mensuales_spotify: int
    activo: bool = True

class CantanteCreate(CantanteBase):
    pass

class CantanteResponse(CantanteBase):
    id: int

class Config:
    orm_mode = True
