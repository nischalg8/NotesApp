from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str
    ALEMBIC_DATABASE_URL: str
    
    model_config = SettingsConfigDict(env_file="infra/.env")

 
settings = Settings()

def get_settings():
    return settings
