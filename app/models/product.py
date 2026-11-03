from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer,Numeric,Boolean
from decimal import Decimal
from app.models.base import Base

class Product(Base):
    __tablename__ = 'product'
    product_id: Mapped[int]=mapped_column(Integer, primary_key=True)
    sku: Mapped[str]=mapped_column(String,nullable=False, unique=True)
    name: Mapped[str]=mapped_column(String,nullable=False)
    description: Mapped[str | None]=mapped_column(String,nullable=True)
    price: Mapped[Decimal]=mapped_column(Numeric(10,2),nullable=False)
    is_active: Mapped[bool]=mapped_column(Boolean,server_default="true")

