from sqlalchemy import Column, Integer, String, Float, Boolean
from api.dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    available = Column(Boolean, default=True)