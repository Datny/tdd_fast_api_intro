import logging

import uvicorn
from fastapi import FastAPI

from app.api import home, summaries
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    app = FastAPI()
    app.include_router(home.router)
    app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
    return app


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up ...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shuting down ...")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
