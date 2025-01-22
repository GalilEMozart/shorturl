import logging

from fastapi import FastAPI

from src.api.routes import create_short_url, main_route, url_redirection
from src.cache.cache import CacheMiddleware
from src.config import logger
from src.db.database import Base, engine

# Désactiver les logs de FastAPI et SQLAlchemy
logging.getLogger("uvicorn").setLevel(logging.WARNING)
logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
# logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy.engine.Engine").disabled = True


# initialize the database
async def lifespan(app: FastAPI):

    logger.info("Creating database tables")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield  # Point entre le démarrage et l'arrêt

    # Arrêt de l'application : nettoyage si nécessaire
    await engine.dispose()
    logger.info("Database connection closed")


app = FastAPI(lifespan=lifespan)

app.add_middleware(CacheMiddleware)

app.include_router(create_short_url.router, tags=["creation"])
app.include_router(url_redirection.router, tags=["redirection"])
app.include_router(main_route.router, tags=["main_route"])
