from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from src.config import load_config


def get_api_key_header():
    config = load_config()
    return APIKeyHeader(name=config.api_token.api_key_name, auto_error=False)


async def get_api_key(api_key_header: str = Security(get_api_key_header())):
    config = load_config()
    if api_key_header != config.api_token.api_key:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
