"""Project configs and settings"""
from typing import List, Optional, Any
import os
from pathlib import Path
from pydantic import RedisDsn, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

import logging


# LOGGING
logging.basicConfig(level=20)
logger = logging.getLogger("main")


class Settings(BaseSettings):
    # GLOBAL
    PROJECT_NAME: str
    VERSION: str
    APP_PATH: Optional[str] = None
    SENTRY_URL: str

    # UVICORN SETTINGS
    SERVER_HOST: str
    SERVER_PORT: int

    # SECURITY
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    SECRET_KEY: str

    # DATABASE
    PG_HOST: str
    PG_USER: str
    PG_PASSWORD: str
    PG_DB_NAME: str
    PG_DSN: Optional[str] = None

    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_DB: int
    REDIS_DSN: Optional[str] = None

    # AVIABIT
    AB_HOST: str

    # CALENDAR
    OAUTHLIB_INSECURE_TRANSPORT: int = 1
    CALENDAR_ID: str
    TIMEZONE: str
    LOCATION: str
    SCOPES: List[str] = ['https://www.googleapis.com/auth/calendar']
    REFRESH_DELAY: int
    REMINDER_DELAY: int

    model_config = SettingsConfigDict(
        env_file='../.env',
        env_file_encoding='utf-8'
    )

    def __init__(self, **values: Any):
        super().__init__(**values)
        self.APP_PATH: str = str(Path(__file__).resolve().parent.parent)
        self.PG_DSN: PostgresDsn = (
            f"postgresql+asyncpg://"
            f"{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}/{self.PG_DB_NAME}"
        )
        self.REDIS_DSN: RedisDsn = (
            f"redis://:"
            f"{self.REDIS_PASSWORD}@{self.REDIS_HOST}/{self.REDIS_DB}"
        )


settings = Settings()


