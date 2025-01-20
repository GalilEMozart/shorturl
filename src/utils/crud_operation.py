from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from src.db.model import Stat_url, Url, User
from src.utils.url_generator_algo import Url_generator_algo


class Data_base_operation:

    @staticmethod
    async def create_user(db: Session, username: str) -> None:

        # user = await db.query(User).filter(User.username==username).first()
        user = await db.execute(select(User).where(User.username == username))
        user = user.scalars().first()

        if not user:
            user = User(username=username)
            db.add(user)
            await db.commit()
            await db.refresh(user)

    @staticmethod
    async def create_short_url(db: Session, original_url: str) -> None:

        generator = Url_generator_algo(6)

        existing_url = await db.execute(
            select(Url).where(Url.original_url == original_url)
        )
        existing_url = existing_url.scalars().first()

        if existing_url:
            raise ValueError("Long url already exists !")

        short_url = None
        existing_short_url = ""

        while not (existing_short_url is None):

            short_url = generator.get_random_url_base62()
            existing_short_url = await db.execute(
                select(Url).where(Url.short_url == short_url)
            )
            existing_short_url = existing_short_url.scalars().first()

        url = Url(short_url=short_url, original_url=original_url)
        db.add(url)
        await db.commit()
        await db.refresh(url)

        return {"original_url": original_url, "short_url": short_url}

    @staticmethod
    async def get_original_url(db: Session, short_url: str):

        original_url = await db.execute(
            select(Url).where(Url.short_url == short_url)
        )
        original_url = original_url.scalars().first()

        if not original_url:
            raise ValueError("Short url doesn't exist")

        return {"original_url": original_url.original_url}

    @staticmethod
    async def add_stat(db: Session, short_url: str, ip_address: str):

        url = Stat_url(short_url=short_url, ip_address=ip_address)
        db.add(url)
        await db.commit()
        await db.refresh(url)
