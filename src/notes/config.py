from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str

    class Config:
        env_file = "infra/.env"

settings = Settings()

def get_settings():
    return settings
