from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.customer_model import Customer
from models.product_model import Product
from models.order_model import Order
import datetime

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            customer_id = order_data['customer_id']
            customer = session.get(Customer, customer_id)

            if not customer: raise ValueError(f"Customer with ID {customer_id} does not exist")

            product_ids = [prod['id'] for prod in order_data['products']]
            product_query = select(Product).where(Product.id.in_(product_ids))
            products = session.execute(product_query).scalars().all()

            if len(product_ids) != len(products): raise ValueError("One or more products do not exist")

            today = datetime.date.today()
            new_order = Order(
                customer_id=order_data['customer_id'],
                order_dt=today,
                products=products,
                status="placed",
                expected_dt= today + datetime.timedelta(days=14)) # Default to two weeks from today
            
            session.add(new_order)
            session.commit()

        session.refresh(new_order)

        for product in new_order.products: session.refresh(product)

        return new_order

def find_all(): return db.session.execute(select(Order)).scalars().all()

def find_by_id(order_id):
    query = select(Order).where(Order.id == order_id)
    return db.session.execute(query).scalar()