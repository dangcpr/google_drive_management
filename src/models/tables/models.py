from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from src.init.db import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(512), unique=True, index=True)
    hashed_password = Column(String(512))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Search_History(Base):
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True)
    search_query = Column(String(512), index=True)
    status_code = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    time = Column(DateTime(timezone=True), server_default=func.now())