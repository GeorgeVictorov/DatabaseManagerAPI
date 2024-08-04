import logging

import uvicorn
from fastapi import FastAPI

from src.models import ParserConfig
from src.database import Database
from src.logger import setup_logger
from src.resources import router


def get_app():
    application = FastAPI()
    application.include_router(router)
    return application


app = get_app()


@app.get("/")
async def root():
    return 'Novorossiysk 1968'


if __name__ == "__main__":
    try:
        setup_logger()  # Configure the logger
        logging.info('Logger is set up successfully.')
    except Exception as e:
        print(f'Logger setup failed: {e}')
        exit(1)

    try:
        database = Database()  # Initialize Database instance
        ParserConfig.metadata.create_all(bind=database.engine)
        logging.info('Tables created successfully.')
    except Exception as e:
        logging.error(f'Error initializing tables: {e}')
        exit(1)

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=False)
