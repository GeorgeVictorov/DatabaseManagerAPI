from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import get_db

router = APIRouter()


@router.get("/")
async def root():
    return 'Novorossiysk 1968'


@router.get("/get_configs/", response_model=list[schemas.ResourceConfig])
def read_resources(db: Session = Depends(get_db)):
    resources = crud.get_resources(db)
    return resources


@router.post("/add_new_config/", response_model=schemas.ResourceConfig)
def create_resource(resource: schemas.ResourceConfigCreate, db: Session = Depends(get_db)):
    db_resource = models.ParserConfig(name=resource.name, url=resource.url, destination=resource.destination)
    try:
        resource = crud.create_resource(db=db, resource=db_resource)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return resource


@router.delete("/rm_config/{resource_id}", response_model=schemas.ResourceConfig)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = crud.delete_resource(db=db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource
