# app/models/meeting_room.py

# Импортируем из Алхимии нужные классы.
from sqlalchemy import Column, String

# Импортируем базовый класс для моделей.
from app.core.db import Base


class MeetingRoom(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255, nullable=False))
