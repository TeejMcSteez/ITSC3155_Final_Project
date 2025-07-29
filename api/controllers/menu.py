from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.menu import MenuItem
from api.schemas.menu import MenuItemCreate

def create_menu_item(db: Session, item: MenuItemCreate):
    if db.query(MenuItem).filter(MenuItem.name == item.name).first():
        raise HTTPException(status_code=400, detail="Menu item with this name already exists.")
    db_item = MenuItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item