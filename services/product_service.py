from sqlalchemy.orm import Session
from sqlalchemy import update
from database import db
from models.product_model import Product

def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product

def find(page, per_page, search_term=None):
    query = db.select(Product)
    if search_term: query = query.where(Product.name.ilike(f"%{search_term}%"))
    query = query.limit(per_page).offset((page-1)*per_page)
    return db.session.execute(query).scalars().all()

def find_by_id(product_id):
    with Session(db.engine) as session: return session.get(Product, product_id)

def get_product(product_id): return db.session.get(Product, product_id)

def update_product(product_id, product):
    with Session(db.engine) as session:
        with session.begin():
            session.execute(update(Product).where(Product.id == product_id).values(**product))
            session.commit()
    return session.query(Product).get(product_id)

def delete_product(product_id):
    with Session(db.engine) as session:
        with session.begin():
            product = session.query(Product).get(product_id)
            if product is None: return False
            session.delete(product)
            session.commit()
            return True