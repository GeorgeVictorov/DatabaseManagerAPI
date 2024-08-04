import logging

from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from .config import load_config


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._engine = create_engine(load_config().postgres.postgres_url, echo=False)
            self._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
            self._initialized = True

    @property
    def engine(self):
        return self._engine

    def get_db(self):
        with self._SessionLocal() as session:
            yield session


class Base(DeclarativeBase):
    pass
