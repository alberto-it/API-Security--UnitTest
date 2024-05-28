from database import db

class CartItem(db.Model):
    __tablename__ = "cart_products"

    customer_id = db.Column(db.ForeignKey('customers.id'), primary_key=True)
    product_id = db.Column(db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<CartItem customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity}>"
