import os

import uvicorn
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.config import get_settings, Settings

app = FastAPI()

register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["models.tortoise"]},
    generate_schemas=False,
    add_exception_handlers=True,
)


@app.get("/")
async def home(settings: Settings = Depends(get_settings)):
    return {
        "hello_santa": "Y",
        "environment": settings.environment,
        "testing": settings.testing,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
