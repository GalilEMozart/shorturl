from fastapi import APIRouter

from src.config import logger

router = APIRouter()


@router.get("/")
def read_root():
    logger.info("Request to the root endpoint")
    return {"Hello": "World, welcome to the URL shortener API"}
