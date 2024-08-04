from pydantic import BaseModel


class ResourceConfigBase(BaseModel):
    name: str
    url: str
    destination: str


class ResourceConfigCreate(ResourceConfigBase):
    pass


class ResourceConfigUpdate(ResourceConfigBase):
    pass


class ResourceConfig(ResourceConfigBase):
    resource_id: int

    class ConfigDict:
        from_attributes = True
