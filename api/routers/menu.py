from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.schemas.menu import MenuItemCreate, MenuItemResponse
from api.controllers.menu import create_menu_item

router = APIRouter(prefix="/menu", tags=["menu"])

@router.post("/", response_model=MenuItemResponse)
def create_menu(item: MenuItemCreate, db: Session = Depends(get_db)):
    return create_menu_item(db, item)