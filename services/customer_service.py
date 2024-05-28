from sqlalchemy.orm import Session
from sqlalchemy import select, update
from database import db
from models.customer_model import Customer
from werkzeug.security import generate_password_hash, check_password_hash
from utils.util import encode_token

def get_token(username, password):
    query = db.select(Customer).where(Customer.username == username)
    customer = db.session.execute(query).scalars().first()
    if customer and check_password_hash(customer.password, password):
        return encode_token(customer.id)

def save(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            sql = select(Customer).where(Customer.username == customer_data['username'])
            username_found = session.execute(sql).scalars().first()
            if username_found: raise ValueError("Customer with that username already exists")
            customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=generate_password_hash(customer_data['password']))
            session.add(customer)
            session.commit()
        session.refresh(customer)
        return customer

def find_all(page, per_page):
    query = db.select(Customer).offset((page-1) * per_page).limit(per_page)
    customers = db.session.execute(query).scalars().all()
    return customers

def get_customer(customer_id): return db.session.get(Customer, customer_id)

def update_customer(customer_id, customer):
    with Session(db.engine) as session:
        with session.begin():
            session.execute(update(Customer).where(Customer.id == customer_id).values(**customer))
            session.commit()
    return session.query(Customer).get(customer_id)

def delete_customer(customer_id):
    with Session(db.engine) as session:
        with session.begin():
            customer = session.query(Customer).get(customer_id)
            if customer is None: return False
            session.delete(customer)
            session.commit()
            return True