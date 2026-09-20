from fastapi import FastAPI

from .database import Base, engine
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Spotify Clone")


@app.get("/")
def home():
    return {"message": "Spotify clone is running!"}