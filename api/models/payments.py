from sqlalchemy import Column, ForeignKey, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_details_id = Column(Integer, ForeignKey("order_details.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    menu_items_id = Column(Integer, ForeignKey("menu_items.id"))
    price = Column(Float)
    isPaid = Column(Boolean, default=False)

    order_details = relationship("OrderDetail", back_populates="payments")
    menu_items = relationship("MenuItem", back_populates="payments")