from app.database import Base, engine
from app.seeding import seed_if_empty

Base.metadata.create_all(bind=engine)
seed_if_empty()