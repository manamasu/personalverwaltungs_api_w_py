from dotenv import load_dotenv
from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DBNAME: str
    DATABASE_URL: str
    HOST: str  # Host for the run.py
    PORT: int  # PORT in run.py
    SECRET_KEY: str  # JWT
    ALGORITHM: str  # JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int  # JWT
    REFRESH_TOKEN_EXPIRE_DAYS: int  # JWT

    @property
    def database_url(self) -> str:
        return self.DATABASE_URL.format(
            POSTGRES_USER=self.POSTGRES_USER,
            POSTGRES_PASSWORD=self.POSTGRES_PASSWORD,
            POSTGRES_SERVER=self.POSTGRES_SERVER,
            POSTGRES_PORT=self.POSTGRES_PORT,
            POSTGRES_DBNAME=self.POSTGRES_DBNAME,
        )

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
