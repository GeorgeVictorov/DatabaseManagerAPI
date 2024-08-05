from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from typing import cast
from .models import ParserConfig


def get_resources(db: Session):
    try:
        return db.query(ParserConfig).order_by(ParserConfig.resource_id.asc()).all()
    except SQLAlchemyError:
        raise RuntimeError(f"A database error occurred.")


def create_resource(db: Session, resource: ParserConfig):
    try:
        existing_resource = db.query(ParserConfig).filter(
            (cast("ColumnElement[bool]", ParserConfig.name == resource.name) | (ParserConfig.url == resource.url))
        ).first()
        if existing_resource:
            raise ValueError("Resource with the same name or url already exists.")

        db.add(resource)
        db.commit()
        db.refresh(resource)
        return resource
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"A database error occurred.")


def delete_resource(db: Session, resource_id: int):
    try:
        resource = db.query(ParserConfig).filter(
            cast("ColumnElement[bool]", ParserConfig.resource_id == resource_id)).first()
        if resource:
            db.delete(resource)
        db.commit()
        return resource
    except SQLAlchemyError:
        db.rollback()
        raise RuntimeError(f"A database error occurred.")
