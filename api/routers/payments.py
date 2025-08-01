from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import payments as controller
from ..schemas import payments as schema

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)

@router.post("/{order_details_id}", response_model=schema.PaymentsCreate)
def create(request: schema.PaymentsCreate, order_details_id, db: Session = Depends(get_db)):
    return controller.create(db=db, order_details_id=order_details_id, request=request)

@router.get("/", response_model=list[schema.PaymentsBase])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.PaymentsBase)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.PaymentsUpdate)
def update(item_id: int, request: schema.PaymentsUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)
# Removing for now as it isnt needed
# @router.delete("/{item_id}")
# def delete(item_id: int, db: Session = Depends(get_db)):
#     return controller.delete(db=db, item_id=item_id)