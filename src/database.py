from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

from .config import load_config

DATABASE_URL = load_config().postgres.postgres_url

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


def get_db():
    with Session() as session:
        yield session
