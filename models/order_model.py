from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from typing import List
from models.order_product import order_product
from sqlalchemy import String

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    order_dt: Mapped[datetime.date] = mapped_column(db.Date)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'), nullable=False)
    customer: Mapped['Customer'] = db.relationship(back_populates='orders')
    products: Mapped[List['Product']] = db.relationship(secondary=order_product)

    status: Mapped[str] = mapped_column(String(255)) 
    expected_dt: Mapped[datetime.date] = mapped_column() 

    def __repr__(self): return f"<Order {self.id} - {self.customer.name}>"