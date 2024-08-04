import logging

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import Database
from .dependencies import get_api_key

router = APIRouter(dependencies=[Depends(get_api_key)])
database = Database()


@router.get("/get_configs/", response_model=list[schemas.ResourceConfig])
def read_resources(db: Session = Depends(database.get_db)):
    try:
        resources = crud.get_resources(db)
        logging.info("Successfully retrieved resources.")
        return resources
    except Exception as e:
        logging.error(f"Failed to retrieve resources: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/add_new_config/", response_model=schemas.ResourceConfig)
def create_resource(resource: schemas.ResourceConfigCreate, db: Session = Depends(database.get_db)):
    db_resource = models.ParserConfig(name=resource.name, url=str(resource.url), destination=resource.destination)
    try:
        created_resource = crud.create_resource(db=db, resource=db_resource)
        logging.info(f"Resource created successfully: {created_resource}")
        return created_resource
    except ValueError as e:
        logging.warning(f"Failed to create resource: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Error occurred while creating resource: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete("/rm_config/{resource_id}", response_model=schemas.ResourceConfig)
def delete_resource(resource_id: int, db: Session = Depends(database.get_db)):
    try:
        resource = crud.delete_resource(db=db, resource_id=resource_id)
        if resource is None:
            logging.warning(f"Resource with ID {resource_id} not found for deletion.")
            raise HTTPException(status_code=404, detail="Resource not found")
        logging.info(f"Resource with ID {resource_id} deleted successfully.")
        return resource
    except Exception as e:
        logging.error(f"Error occurred while deleting resource with ID {resource_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
