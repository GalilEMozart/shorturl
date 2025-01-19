from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World, welcome to the URL shortener API"}
