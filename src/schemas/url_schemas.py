from pydantic import BaseModel

class Create_Base(BaseModel):
    """ Model for user """
    username:str
    original_url:str

class UrlShortBase(BaseModel):
    """ Model for short url """
    short_url:str


