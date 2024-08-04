from dataclasses import dataclass
from environs import Env

CONFIG_TABLE_NAME: str = 'resource_config'


@dataclass
class PostgresConfig:
    postgres_url: str


@dataclass
class Config:
    postgres: PostgresConfig


def load_config(path: str = '.env') -> Config:
    """
    Load the configuration from the specified .env file.

    Args:
        path (str): The path to the .env file.

    Returns:
        Config: The configuration object with loaded settings.
    """
    env: Env = Env()
    env.read_env(path)

    return Config(postgres=PostgresConfig(
        postgres_url=env('DATABASE_URL'),
    ))
