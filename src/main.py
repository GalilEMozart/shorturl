from fastapi import FastAPI
from src.db.database import Base, engine, get_db

# initialize the database
Base.metadata.create_all(bind=engine)
get_db()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World, welcome to the URL shortener API"}

 