from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer,DateTime, func
from datetime import datetime
from app.models.base import Base

class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    email: Mapped[str] = mapped_column(String(255),unique=True,nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255),nullable=False)
    first_name: Mapped[str] = mapped_column(String(100),nullable=False)
    last_name: Mapped[str] = mapped_column(String(100),nullable=False)
    phone: Mapped[str | None] = mapped_column(String(20),nullable=True)
    role: Mapped[str] = mapped_column(String(50), server_default="customer")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())