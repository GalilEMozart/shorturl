from pydantic_settings import BaseSettings


class Config(BaseSettings):

    # redis settings
    cache_enabled: bool = True
    redis_host: str = "redis"
    redis_port: int = 6379
    redis_db: int = 0
    cache_expire: int = 120

    # postgres settings
    postgres_host: str = "db"
    postgres_db: str = "postgres"
    postgres_user: str = "postgres"
    postgres_password: str = "password"

    class Config:
        env_file = ".env"


settings = Config()
