from database import db
from models.cart_products import CartItem
from models.product_model import Product

class ShoppingCartService:

    def save(self, customer_id, product_id, quantity):
        if db.session.query(Product).get(product_id):
            existing_item = CartItem.query.filter_by(customer_id=customer_id, product_id=product_id).first()
            if existing_item:
                existing_item.quantity += quantity
                if existing_item.quantity < 0: existing_item.quantity = 0
            else:
                new_item = CartItem(customer_id=customer_id, product_id=product_id, quantity=quantity)
                db.session.add(new_item)
            db.session.commit()
