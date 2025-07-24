from fastapi import APIRouter, Depends, exceptions, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..controllers import sandwiches
from ..schemas import order_details
from ..schemas import sandwiches as sandwich
from ..dependencies.database import engine, get_db

routers = APIRouter(
    tags = ['Payments'],
    prefix="/payments"
)



@routers.post("/payments/{order_id}{payment}", response_model=order_details.OrderDetail)
def process_payment(order_id: int, payment: float, response_model=order_details.OrderDetail, db: Session = Depends(get_db)):
    
    order = controller.read_one(db, order_id)
    sandwich_id = order.sandwich_id
    sandwich_obj = sandwiches.read_one(db, sandwich_id)

    if sandwich_obj is None:
        raise exceptions.HTTPException(status_code=404, detail="Sandwich not found")
    total = payment - sandwich_obj.price  # type: ignore

    if total < 0:
        raise exceptions.HTTPException(status_code=400, detail="Payment is less than order amount")
    return order

