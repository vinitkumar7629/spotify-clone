from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Spotify Clone")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return {"message": "Spotify clone is running!"}


@app.get("/api/songs", response_model=list[schemas.SongOut])
def list_songs(db: Session = Depends(get_db)):
    return db.query(models.Song).all()