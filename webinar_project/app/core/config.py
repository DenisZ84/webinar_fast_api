import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Вебинар по Fast API'
    db_url: str = 'postgresql+asyncpg://{0}:{1}@db:5432/{2}'.format(
        os.getenv('POSTGRES_USER'),
        os.getenv('POSTGRES_PASSWORD'),
        os.getenv('POSTGRES_DB'),
    )
    path: str

    class Config:
        env_file = '.env'

settings = Settings()