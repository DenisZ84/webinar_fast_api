from sqlalchemy import Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, declared_attr
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core.config import settings

class PreBase:

    @declared_attr
    def __tablename__(cls):
        # Именем таблицы будет название модели в нижнем регистре.
        return cls.__name__.lower()

    # Во все таблицы будет добавлено поле ID.
    id = Column(Integer, primary_key=True)

Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.db_url)

async_session = AsyncSession(engine)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
