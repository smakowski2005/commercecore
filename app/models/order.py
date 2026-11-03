from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer,DateTime,ForeignKey, func
from datetime import datetime
from app.models.base import Base

class Order(Base):
    __tablename__ = "order"
    order_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.user_id"))
    status: Mapped[str] = mapped_column(String(50),server_default="PENDING")
    created_at: Mapped[datetime] = mapped_column(DateTime,server_default=func.now())
