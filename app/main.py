import os

import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import home


def create_application() -> FastAPI:
    app = FastAPI()

    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )

    app.include_router(home.router)
    return app


app = create_application()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
