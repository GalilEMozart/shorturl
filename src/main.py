from fastapi import FastAPI
from src.api.routes import create_short_url, url_redirection, main_route

from src.db.database import Base, engine
from src.cache.cache import CacheMiddleware

# initialize the database
async def lifespan(app: FastAPI):
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    

    yield  # Point entre le démarrage et l'arrêt

    # Arrêt de l'application : nettoyage si nécessaire
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(CacheMiddleware)

app.include_router(create_short_url.router, tags=["creation"])
app.include_router(url_redirection.router, tags=["redirection"])
app.include_router(main_route.router,tags=["main_route"])


 