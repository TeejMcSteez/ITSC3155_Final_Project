from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    menu_items_id = Column(Integer, ForeignKey("menu_items.id"))
    amount = Column(Integer, index=True, nullable=False)
    tracking_number = Column(String(36), unique=True)
    type = Column(String(20))
    status = Column(String(20))

    payments = relationship("Payments", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
    menu_items = relationship("MenuItem", back_populates="order_details")
