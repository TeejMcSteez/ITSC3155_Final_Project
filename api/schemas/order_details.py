from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .menu import MenuItem


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    menu_item_id: int
    type: str
    status: str

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    amount: Optional[int] = None
    status: Optional[str] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    tracking_number: str
    type: str
    status: str
    menu_item: Optional[MenuItem] = None

    class ConfigDict:
        from_attributes = True