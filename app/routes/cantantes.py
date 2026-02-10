from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.cantante import Cantante
from app.schemas.cantante import CantanteCreate, CantanteResponse

router = APIRouter(
    prefix="/cantantes",
    tags=["cantantes"]
)

@router.get("/", response_model=list[CantanteResponse])
def get_cantantes(db: Session = Depends(get_db)):
    return db.query(Cantante).all()

@router.get("/{cantante_id}", response_model=CantanteResponse)
def get_cantante(cantante_id: int, db: Session = Depends(get_db)):
    cantante = db.query(Cantante).filter(Cantante.id == cantante_id).first()
    if not cantante:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cantante no encontrado"
        )
    return cantante

@router.post("/", response_model=CantanteResponse, status_code=status.HTTP_201_CREATED)
def create_cantante(cantante: CantanteCreate, db: Session = Depends(get_db)):
    existing_cantante = db.query(Cantante).filter(Cantante.nombre == cantante.nombre).first()
    if existing_cantante:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El cantante ya existe"
        )

    new_cantante = Cantante(**cantante.dict())
    db.add(new_cantante)
    db.commit()
    db.refresh(new_cantante)
    return new_cantante

@router.put("/{cantante_id}", response_model=CantanteResponse)
def update_cantante(cantante_id: int, cantante: CantanteCreate, db: Session = Depends(get_db)):
    stored_cantante = db.query(Cantante).filter(Cantante.id == cantante_id).first()
    if not stored_cantante:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cantante no encontrado"
        )

    for key, value in cantante.dict().items():
        setattr(stored_cantante, key, value)

    db.add(stored_cantante)
    db.commit()
    db.refresh(stored_cantante)
    return stored_cantante

@router.delete("/{cantante_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cantante(cantante_id: int, db: Session = Depends(get_db)):
    cantante = db.query(Cantante).filter(Cantante.id == cantante_id).first()
    if not cantante:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cantante no encontrado"
        )
    db.delete(cantante)
    db.commit()
