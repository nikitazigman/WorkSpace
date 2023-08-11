from functools import lru_cache
from pydantic import Field
from pydantic_settings import SettingsConfigDict, BaseSettings
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent.parent


class AppSettings(BaseSettings):
    redis_host: str = Field(alias="REDIS_HOST")
    redis_port: int = Field(alias="REDIS_PORT")
    redis_user: str = Field(alias="REDIS_USER")
    redis_password: str = Field(alias="REDIS_PASS")

    app_host: str = Field(alias="APP_HOST")
    app_port: int = Field(alias="APP_PORT")

    debug: bool = Field(alias="DEBUG")

    model_config = SettingsConfigDict(env_file=ROOT_DIR / ".env")


@lru_cache(maxsize=1)
def get_app_settings() -> AppSettings:
    return AppSettings()  # type: ignore
