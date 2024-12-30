from fastapi import HTTPException, APIRouter, Depends, status






router = APIRouter()



@router.get("/{short_url}")
async def get_url(short_url:str):
    return {"short_url":short_url}

@router.post("/create/{username}/{long_url}/{email}")
async def create_url(username:str, long_url:str, email:str):
    return {"username":username, "long_url":long_url, "email":email}