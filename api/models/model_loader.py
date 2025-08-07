from . import orders, order_details, payments

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
