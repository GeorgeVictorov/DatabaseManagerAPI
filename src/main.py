import logging
import uvicorn

from fastapi import FastAPI

from src.models import ParserConfig
from src.database import engine
from src.logger import setup_logger
from src.resources import router


def get_app():
    application = FastAPI()
    application.include_router(router)
    return application


app = get_app()

if __name__ == "__main__":
    setup_logger()
    ParserConfig.metadata.create_all(bind=engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
