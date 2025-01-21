from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{settings.postgres_user}:"
    f"{settings.postgres_password}@"
    f"{settings.postgres_host}/"
    f"{settings.postgres_db}"
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
