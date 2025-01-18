from pydantic_settings import BaseSettings

class Config(BaseSettings):
    
    cache_enabled: bool = True
    redis_host: str = "localhost"
    redis_port: int  = 6379
    redis_db: int = 0
    cache_expire: int = 120

    class Config:
        env_file = ".env"

settings = Config()
