from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    available: bool

class MenuItemCreate(MenuItemBase):
    name: str
    description: Optional[str] = None
    price: float
    available: Optional[bool] = None

class MenuItemUpdate(MenuItemBase):
    name: str
    description: Optional[str] = None
    price: float
    available: Optional[bool] = None

class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
