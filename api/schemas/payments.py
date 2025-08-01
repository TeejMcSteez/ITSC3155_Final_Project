from pydantic import BaseModel

class PaymentsBase(BaseModel):
    order_details_id: int
    order_id: int
    sandwich_id: int
    isPaid: bool = False

class PaymentsCreate(BaseModel):
    pass

class PaymentsUpdate(BaseModel):
    isPaid: bool = True

class PaymentsSchema(BaseModel):
    id: int
    order_details_id: int
    order_id: int
    sandwich_id: int
    isPaid: bool

    class ConfigDict:
        from_attributes = True