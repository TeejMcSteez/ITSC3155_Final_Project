from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import payments as model
from sqlalchemy.exc import SQLAlchemyError
# Used to auto-fill price from db
from ..controllers import orders, order_details, menu



def create(db: Session, order_details_id, request):
    od = order_details.read_one(db, order_details_id)
    if od is None:
        raise HTTPException(status_code=404, detail="Order not found!")
    
    menu_item = menu.read_one(db, od.menu_items_id)
    if menu_item is None:
        raise HTTPException(status_code=404, detail="Sandwich not found!")
    
    new_item = model.Payments(
        order_details_id=order_details_id,
        order_id=od.order_id,
        menu_items_id=od.menu_items_id,
        price=menu_item.price,
        isPaid = False
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    return new_item

def read_all(db: Session):
    try:
        result = db.query(model.Payments).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id):
    try:
        item = db.query(model.Payments).filter(model.Payments.id == item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item
# TODO
# I think this is wrong I dont need to pass a dict just to flip the boolean
def update(db: Session, item_id, request):
    try:
        item = db.query(model.Payments).filter(model.Payments.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()
# Added for sake of keeping spec, but deleting payment history isn't a good idea more than likely
# Won't add a route for it but will be a controller in case their needs to be an auditing process
def delete(db: Session, item_id):
    try:
        item = db.query(model.Payments).filter(model.Payments.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_revenue(db: Session):
    try:
        payments = db.query(model.Payments).where(model.Payments.isPaid == True).all()
        total = 0
        for payment in payments:
            total += payment.price
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return total