from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


#SQLALCHEMY_DATABASE_URL = "postgresql://postgres@localhost/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/postgres"


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
    )

Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
