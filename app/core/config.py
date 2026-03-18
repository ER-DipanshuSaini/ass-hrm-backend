from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "HRMS Lite"
    DEBUG_MODE: bool = True
    DATABASE_URL: str = "sqlite:///./hrms-lite.db"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
