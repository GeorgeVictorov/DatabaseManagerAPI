import logging
from typing import cast

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.models import ParserConfig
from src.database import Database
from src.logger import setup_logger
from src.resources import router


def get_app():
    application = FastAPI()

    application.add_middleware(
        cast("_MiddlewareClass[P]", CORSMiddleware),
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router, tags=['database'])
    application.mount("/static", StaticFiles(directory="static"), name="static")

    # Serve index.html at the root path
    @application.get("/", include_in_schema=False)
    async def read_index():
        return FileResponse("static/index.html")

    return application


app = get_app()

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
