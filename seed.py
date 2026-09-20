from app.database import SessionLocal, Base, engine
from app.models import Song

Base.metadata.create_all(bind=engine)

songs = [
    Song(title="Song One", artist="Artist A", album="Single",
         audio_file="/static/audio/track1.mp3"),
    Song(title="Song Two", artist="Artist B", album="Single",
         audio_file="/static/audio/track2.mp3"),
    Song(title="Song Three", artist="Artist C", album="Single",
         audio_file="/static/audio/track3.mp3"),
]

db = SessionLocal()

if db.query(Song).count() == 0:
    db.add_all(songs)
    db.commit()
    print("Added", len(songs), "songs")
else:
    print("Songs already exist, nothing added")

db.close()