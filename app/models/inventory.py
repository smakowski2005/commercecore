from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, CheckConstraint
from app.models.base import Base

class Inventory(Base):
    __tablename__ = 'inventory'
    __table_args__ = (
        CheckConstraint('available_quantity >= 0', name='check_available_quantity_positive'),
    )
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'), primary_key=True)
    available_quantity: Mapped[int] = mapped_column(Integer, default=0)