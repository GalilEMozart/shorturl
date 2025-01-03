from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.utils.crud_operation import Data_base_operation
from src.schemas.url_schemas import Create_Base

router = APIRouter()

@router.post("/create_url/")
def create_short_url(url_data_information:Create_Base,db:Session=Depends(get_db)):
    try:
        Data_base_operation.create_user(db, url_data_information.username)
        result = Data_base_operation.create_short_url(db, url_data_information.original_url)

        return result
     
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))