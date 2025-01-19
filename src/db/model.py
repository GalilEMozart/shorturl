from sqlalchemy import Column, ForeignKey, Integer, String, Time, text
from sqlalchemy.orm import relationship

from src.db.database import Base


class User(Base):
    """Table that store user information"""

    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)

    urls = relationship("Url", back_populates="user")


class Url(Base):
    """Table that store url information"""

    __tablename__ = "urls"

    id_url = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("users.id_user"))
    created_at = Column(Time, server_default=text("now()"))
    short_url = Column(String, unique=True, nullable=False, index=True)
    original_url = Column(String, unique=True, nullable=False, index=True)

    user = relationship("User", back_populates="urls")
    stats = relationship("Stat_url", back_populates="url")


class Stat_url(Base):
    """Talbe that store analytics informations about every url"""

    __tablename__ = "stats"

    id_stat = Column(Integer, primary_key=True, autoincrement=True)
    id_url = Column(Integer, ForeignKey("urls.id_url"))
    short_url = Column(String)
    redirected_at = Column(Time, server_default=text("now()"))
    ip_address = Column(String)

    url = relationship("Url", back_populates="stats")
