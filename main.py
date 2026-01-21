from fastapi import FastAPI

from database.database import Base, engine
from routes import cantantes, albumes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(cantantes.router)
app.include_router(albumes.router)

@app.get("/")
def root():
    return {"message": "API de Cantantes y Álbumes con FastAPI y SQLite"}
