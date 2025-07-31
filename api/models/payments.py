from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_details_id = Column(Integer, ForeignKey("order_details.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    price = Column(Float, ForeignKey("sandwiches.price"))

    order_details = relationship("Order Details", back_populates="order_details")
    sandwich = relationship("Sandwich", back_populates="sandwiches")
