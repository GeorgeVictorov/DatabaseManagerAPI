from sqlalchemy import Column, Integer, String
from .config import CONFIG_TABLE_NAME
from .database import Base


class ParserConfig(Base):
    __tablename__ = CONFIG_TABLE_NAME

    resource_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False, unique=True)
    destination = Column(String, nullable=False)
