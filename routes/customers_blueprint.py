from flask import Blueprint
from controllers.customer_controller import (
    save_customer,
    find_all_customers,  
    find_customer_by_id,
    update_customer,
    delete_customer,
)

customer_bp = Blueprint("customer_bp", __name__)

customer_bp.add_url_rule('/', methods=['POST'], view_func=save_customer)
customer_bp.add_url_rule('/', methods=['GET'], view_func=find_all_customers)
customer_bp.add_url_rule('/<int:customer_id>', methods=['GET'], view_func=find_customer_by_id)
customer_bp.add_url_rule('/<int:customer_id>', methods=['PUT'], view_func=update_customer)
customer_bp.add_url_rule('/<int:customer_id>', methods=['DELETE'], view_func=delete_customer)
