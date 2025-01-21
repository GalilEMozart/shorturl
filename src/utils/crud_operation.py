from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from src.config import logger
from src.db.model import Stat_url, Url, User
from src.utils.url_generator_algo import Url_generator_algo


class Data_base_operation:

    @staticmethod
    async def create_user(db: Session, username: str) -> None:

        # user = await db.query(User).filter(User.username==username).first()
        logger.info(f"Creating user {username}")
        user = await db.execute(select(User).where(User.username == username))
        user = user.scalars().first()

        if not user:
            user = User(username=username)
            db.add(user)
            await db.commit()
            await db.refresh(user)
            logger.info(f"User {username} created")
        else:
            logger.error(f"User {username} already exists")

    @staticmethod
    async def create_short_url(db: Session, original_url: str) -> None:

        logger.info(f"Creating short url for {original_url}")
        generator = Url_generator_algo(6)

        existing_url = await db.execute(
            select(Url).where(Url.original_url == original_url)
        )
        existing_url = existing_url.scalars().first()

        if existing_url:
            logger.error("Long url already exists !")
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

        logger.info(f"Short url for {original_url} created, is {short_url}")

        return {"original_url": original_url, "short_url": short_url}

    @staticmethod
    async def get_original_url(db: Session, short_url: str):

        logger.info(f"Getting original url for {short_url}")
        original_url = await db.execute(
            select(Url).where(Url.short_url == short_url)
        )
        original_url = original_url.scalars().first()

        if not original_url:
            logger.error("Short url doesn't exist")
            raise ValueError("Short url doesn't exist")

        logger.info(
            f"Original url for {short_url} is {original_url.original_url}"
        )
        return {"original_url": original_url.original_url}

    @staticmethod
    async def add_stat(db: Session, short_url: str, ip_address: str):

        logger.info(f"Adding stat for {short_url}")
        url = Stat_url(short_url=short_url, ip_address=ip_address)
        db.add(url)
        await db.commit()
        await db.refresh(url)
