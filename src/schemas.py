from pydantic import BaseModel, HttpUrl


class ResourceConfigBase(BaseModel):
    name: str
    url: HttpUrl
    destination: str


class ResourceConfigCreate(ResourceConfigBase):
    pass


class ResourceConfigUpdate(ResourceConfigBase):
    pass


class ResourceConfig(ResourceConfigBase):
    resource_id: int

    class ConfigDict:
        from_attributes = True
