from sqlalchemy import Column, ForeignKey, Integer, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_details_id = Column(Integer, ForeignKey("order_details.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    sandwich_price = Column(DECIMAL)
    isPaid = Column(Boolean, default=False)

    order_details = relationship("Order Details", back_populates="order_details")
    sandwich = relationship("Sandwich", back_populates="sandwiches")
