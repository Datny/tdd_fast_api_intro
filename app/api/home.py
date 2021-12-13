from fastapi import APIRouter, Depends

from app.config import get_settings, Settings

router = APIRouter()


@router.get("/")
async def home(settings: Settings = Depends(get_settings)):
    return {
        "hello_santa": "Y",
        "environment": settings.environment,
        "testing": settings.testing,
    }