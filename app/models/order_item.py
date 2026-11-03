from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer,ForeignKey, Numeric
from decimal import Decimal
from app.models.base import Base

class OrderItem(Base):
    __tablename__ = "order_item"
    order_id: Mapped[int] = mapped_column(ForeignKey("order.order_id"),primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.product_id"), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer,nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10,2),nullable=False)