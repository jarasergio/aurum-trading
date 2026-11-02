from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Aurum Trading"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True

    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    DATABASE_URL: str

    TRADING_MODE: str = "simulation"
    TRADING_ENABLED: bool = False

    MARKET_DATA_PROVIDER: str = ""
    MARKET_DATA_API_KEY: str = ""

    MARKET_DATA_POLL_INTERVAL: int = 10
    MARKET_DATA_WORKER_ENABLED: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
