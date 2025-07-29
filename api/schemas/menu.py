from pydantic import BaseModel, Field

class MenuItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    price: float = Field(..., gt=0)
    available: bool = True

class MenuItemResponse(MenuItemCreate):
    id: int

    class Config:
        orm_mode = True