from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import or_
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Spotify Clone")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/api/songs", response_model=list[schemas.SongOut])
def list_songs(db: Session = Depends(get_db)):
    return db.query(models.Song).all()


@app.get("/api/songs/search", response_model=list[schemas.SongOut])
def search_songs(q: str = "", db: Session = Depends(get_db)):
    q = q.strip()
    if not q:
        return db.query(models.Song).all()

    pattern = f"%{q}%"
    return db.query(models.Song).filter(
        or_(
            models.Song.title.ilike(pattern),
            models.Song.artist.ilike(pattern),
            models.Song.album.ilike(pattern),
        )
    ).all()