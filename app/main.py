from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from database.database import Base, engine
from routes import cantantes, albumes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(cantantes.router)
app.include_router(albumes.router)

@app.get("/")
def root():
    return {"message": "API de Cantantes y Álbumes con FastAPI y SQLite"}

app.add_middleware(
CORSMiddleware,
allow_origins=[
"http://localhost:5173", # React (Vite)
"http://localhost:5174",
"http://localhost:8000" # React (Create React App)
],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)