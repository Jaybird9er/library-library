import uvicorn
from fastapi import FastAPI

from app.settings import Settings

app = FastAPI()
settings = Settings()


def main():
    uvicorn.run(
        "app.main:app",
        host=settings.host_address,
        port=settings.port,
        log_level="debug",
    )
