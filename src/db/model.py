from database import Base
from sqlalchemy import Column, Integer, String, Time, text

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    api = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    created_at = Column(Time, server_default=text("now()"))
    short_url = Column(String, unique=True, index=True)
    long_url = Column(String, unique=True, index=True)


