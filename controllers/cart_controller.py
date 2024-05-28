from flask import jsonify, request
from services.cart_service import ShoppingCartService
from schemas.cart_schema import ShoppingCartSchema
from models.customer_model import Customer
from models.product_model import Product
from database import db
from models.cart_products import CartItem

cart_schema = ShoppingCartSchema()
cart_service = ShoppingCartService()

def add_to_cart():
    data = request.get_json()
    customer_id = data.get('customer_id')
    customer_exists = db.session.query(Customer).get(customer_id) 
    if not customer_exists: return jsonify({'message': 'Customer not found'}), 400 
    products = data.get('products')
    for product_data in products:
        product_id = product_data.get('id')
        quantity = product_data.get('quantity')
        cart_service.save(customer_id, product_id, quantity)

    return jsonify({'message': 'Products added to cart successfully!'}), 201


def get_cart_by_id(customer_id):
    cart_items = CartItem.query.filter_by(customer_id=customer_id).all()
    if cart_items:
        response_data = {'customer_id': customer_id, 'products': []}
        total = 0
        for item in cart_items:
            product = db.session.query(Product).get(item.product_id) 
            product_data = {
                'id': item.product_id, 
                'quantity': item.quantity,
                'name': product.name,
                'price': product.price
                }
            response_data['products'].append(product_data)
            total += product.price * item.quantity
        response_data['total_price'] = total
        return jsonify(response_data)
    return jsonify({'message': 'No carts found for this customer'}), 404

def remove_from_cart(customer_id, product_id):
    customer_exists = db.session.query(Customer).get(customer_id) 
    if not customer_exists: return jsonify({'message': 'Customer not found'}), 400
    cart_items = CartItem.query.filter_by(customer_id=customer_id).all()
    for item in cart_items:
        if item.product_id == product_id:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'message': 'Item removed from cart'}), 200
    return jsonify({'message': 'Product ID not found for this customer'}), 404

def empty_cart(customer_id):
    customer_exists = db.session.query(Customer).get(customer_id) 
    if not customer_exists: return jsonify({'message': 'Customer not found'}), 400
    confirm = request.args.get('confirm') 
    if confirm == 'yes':
        CartItem.query.filter_by(customer_id=customer_id).delete()
        db.session.commit()
        return jsonify({'message': 'Cart emptied successfully'}), 200
    return jsonify({'message': 'Include confirm=yes to empty cart'}), 405