from aiologger.handlers.files import AsyncFileHandler
from aiologger.loggers.json import JsonLogger  # Logger asynchrone JSON
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

"""
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Handler for file
file_handler = logging.FileHandler("logs/app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Handler for sdtout
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
"""
logger = JsonLogger.with_default_handlers(
    name="async_logger", level="INFO", extra={"service": "CacheMiddleware"}
)
file_handler = AsyncFileHandler(filename="logs/cache_middleware.log")
logger.add_handler(file_handler)
