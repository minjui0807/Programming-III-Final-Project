from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    PROJECT_NAME: str = "記帳系統 API"

    class Config:
        env_file = ".env"

settings = Settings()