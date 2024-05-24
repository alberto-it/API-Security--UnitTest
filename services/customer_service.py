from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.customer_model import Customer
from circuitbreaker import circuit
from werkzeug.security import generate_password_hash, check_password_hash
from utils.util import encode_token

def save(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            customer_query = select(Customer).where(Customer.username == customer_data['username'])
            customer_check = session.execute(customer_query).scalars().first()
            if customer_check is not None:
                raise ValueError("Customer with that username already exists")
            new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=generate_password_hash(customer_data['password']))
            session.add(new_customer)
            session.commit()
        session.refresh(new_customer)
        return new_customer

def find_all():
    query = db.select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers

def get_token(username, password):
    query = db.select(Customer).where(Customer.username == username)
    customer = db.session.execute(query).scalars().first()
    if customer and check_password_hash(customer.password, password):
        return encode_token(customer.id)

def get_customer(customer_id): return db.session.get(Customer, customer_id)