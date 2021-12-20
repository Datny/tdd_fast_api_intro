from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/")
async def home(settings: Settings = Depends(get_settings)):
    return {
        "hello_santa": "Yes",
        "environment": settings.environment,
        "testing": settings.testing,
    }
