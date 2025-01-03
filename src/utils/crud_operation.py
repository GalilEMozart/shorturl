from sqlalchemy.orm import Session
from src.db.model import User, Url, Stat_url
from src.utils.url_generator_algo import Url_generator_algo


class Data_base_operation():

    @staticmethod
    def create_user(db:Session, username:str) -> None:

        user = db.query(User).filter(User.username==username).first()

        if not user:
            user = User(username=username)
            db.add(user)
            db.commit()
            db.refresh(user)

    @staticmethod
    def create_short_url(db:Session, original_url:str) -> None:

        generator = Url_generator_algo(6)

        existing_url = db.query(Url).filter(Url.original_url==original_url).first()
        if existing_url:
            raise ValueError('Long url already exists !')
        
        short_url = None
        existing_short_url = ''

        while not (existing_short_url==None):

            short_url = generator.get_random_url_base62()
            existing_short_url = db.query(Url).filter(Url.short_url==short_url).first()
        
        url= Url(short_url=short_url, original_url = original_url)
        db.add(url)
        db.commit()
        db.refresh(url)

        return {"original_url":original_url, "short_url":short_url}
    
    @staticmethod
    def get_original_url(db:Session, short_url:str):

        original_url = db.query(Url).filter(Url.short_url==short_url).first()
        if not original_url:
            raise ValueError("Short url doesn't exist")

        return {"original_url":original_url.original_url}
        
    @staticmethod
    def add_stat(db:Session, short_url:str, ip_address:str):

        url = Stat_url(short_url=short_url, ip_address = ip_address)
        db.add(url)
        db.commit()
        db.refresh(url)