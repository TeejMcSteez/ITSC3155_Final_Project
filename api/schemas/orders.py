from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    tracking_number: int
    payment_status : bool
    order_type : str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    payment_status: Optional[bool] = None
    order_type: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    tracking_number: int
    payment_status: bool
    order_type: str
    created_at: datetime

    class Config:
        orm_mode = True