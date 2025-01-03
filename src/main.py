from fastapi import FastAPI
from src.api.routes import create_short_url, url_redirection, main_route

from src.db.database import Base, engine

# initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(create_short_url.router, tags=["creation"])
app.include_router(url_redirection.router, tags=["redirection"])
app.include_router(main_route.router,tags=["main_route"])


 