from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    CELERY_BROKER_URL: str

    class Config:
        env_file = ".env"