from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True)
    description = Column(String(255))
    price = Column(Float)
    available = Column(Boolean, default=True)

    payments = relationship("Payments", back_populates="menu_items")
    order_details = relationship("OrderDetail", back_populates="menu_items")