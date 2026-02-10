from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.database import SessionLocal
from models.album import Album
from models.cantante import Cantante
from schemas.album import AlbumCreate, AlbumResponse

router = APIRouter(
    prefix="/albumes",
    tags=["albumes"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[AlbumResponse])
def get_albumes(db: Session = Depends(get_db)):
    return db.query(Album).all()

@router.get("/{album_id}", response_model=AlbumResponse)
def get_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if not album:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Álbum no encontrado"
        )
    return album

@router.post("/", response_model=AlbumResponse, status_code=status.HTTP_201_CREATED)
def create_album(album: AlbumCreate, db: Session = Depends(get_db)):
    # Validar que el cantante existe
    cantante = db.query(Cantante).filter(Cantante.id == album.cantante_id).first()
    if not cantante:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El cantante no existe"
        )
    
    existing_album = db.query(Album).filter(Album.nombre == album.nombre).first()
    if existing_album:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El álbum ya existe"
        )

    new_album = Album(**album.dict())
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album

@router.put("/{album_id}", response_model=AlbumResponse)
def update_album(album_id: int, album: AlbumCreate, db: Session = Depends(get_db)):
    # Validar que el cantante existe
    cantante = db.query(Cantante).filter(Cantante.id == album.cantante_id).first()
    if not cantante:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El cantante no existe"
        )
    
    stored_album = db.query(Album).filter(Album.id == album_id).first()
    if not stored_album:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Álbum no encontrado"
        )

    for key, value in album.dict().items():
        setattr(stored_album, key, value)

    db.add(stored_album)
    db.commit()
    db.refresh(stored_album)
    return stored_album

@router.delete("/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == album_id).first()
    if not album:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Álbum no encontrado"
        )
    db.delete(album)
    db.commit()
