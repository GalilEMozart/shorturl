from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_db
from src.schemas.url_schemas import UrlShortBase
from src.utils.crud_operation import Data_base_operation

router = APIRouter()


@router.post("/get_url")
async def get_original_url(
    short_url: UrlShortBase,
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await Data_base_operation.get_original_url(
            db, short_url.short_url
        )

        # analytics infos
        ip_address = request.client.host
        await Data_base_operation.add_stat(
            db, short_url=short_url.short_url, ip_address=ip_address
        )

        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
