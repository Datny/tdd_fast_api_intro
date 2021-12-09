import uvicorn

from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()


@app.get("/")
async def home(settings: Settings = Depends(get_settings)):
    return {'hello_santa': 'Y',
            'environment': settings.environment,
            'testing': settings.testing}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)