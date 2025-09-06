# Configuration / environment settings
# backend/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Database
    # (You could also move your DATABASE_URL here)

    # JWT
    jwt_secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: int

    # Load from the .env file
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()