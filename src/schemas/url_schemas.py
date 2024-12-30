from pydantic import BaseModel

class UrlBase(BaseModel):
    id: str
    api: int
    username: str
    email: str
    short_url: str
    long_url: str

