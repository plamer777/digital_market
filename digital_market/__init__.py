"""This file contains the EnvSettings class to get access to environment
variables"""
from pydantic import BaseSettings
# ---------------------------------------------------------------------------


class EnvSettings(BaseSettings):
    """This class uploads environment variables"""
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    DEBUG: bool
    TITLE: str
    DESCRIPTION: str
    VERSION: str
    TOKEN_LIFETIME: int
    DJANGO_SECRET: str = None
    IS_ACTIVE: bool = False
    DESCRIPTION_FILE: str = None

    class Config:
        env_file = '.env'


env_sets = EnvSettings()
