from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func, Enum
import enum
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(Text, nullable=False)

    tasks = relationship("Task", back_populates="user")


class TaskStatus(str, enum.Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.new, nullable=False)
    due_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)

    user = relationship("User", back_populates="tasks")