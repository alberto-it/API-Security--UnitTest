from flask import Blueprint
from controllers.cart_controller import (
    add_to_cart,
    get_cart_by_id,
    remove_from_cart,
    empty_cart
)

cart_bp = Blueprint('cart', __name__)

cart_bp.add_url_rule('/', methods=['POST'], view_func=add_to_cart)
cart_bp.add_url_rule('/<int:customer_id>', methods=['GET'], view_func=get_cart_by_id)
cart_bp.add_url_rule('/<int:customer_id>/item/<int:product_id>', methods=['DELETE'], view_func=remove_from_cart)
cart_bp.add_url_rule('/<int:customer_id>', methods=['DELETE'], view_func=empty_cart)
