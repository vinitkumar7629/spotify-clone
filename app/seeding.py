from .database import SessionLocal
from .models import Song

SONGS = [
    {"title": "Football-Football Music", "artist": "SigmaMusicart",
     "album": "Single", "audio_file": "/static/audio/track1.mp3"},
    {"title": "Dark", "artist": "AudioCopper",
     "album": "Single", "audio_file": "/static/audio/track2.mp3"},
    {"title": "Wonders of the Earth", "artist": "Grand_Project",
     "album": "Single", "audio_file": "/static/audio/track3.mp3"},
]


def seed_if_empty():
    db = SessionLocal()
    try:
        if db.query(Song).count() == 0:
            db.add_all([Song(**data) for data in SONGS])
            db.commit()
            print("Added", len(SONGS), "songs")
        else:
            print("Songs already exist, nothing added")
    finally:
        db.close()