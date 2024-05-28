from flask import Blueprint
from controllers.product_controller import (
    create_product, 
    get_products,
    get_product_by_id,
    update_product,
    delete_product,
)

product_bp = Blueprint("product_bp", __name__)

product_bp.add_url_rule("/", methods=["POST"], view_func=create_product)
product_bp.add_url_rule("/", methods=["GET"], view_func=get_products)
product_bp.add_url_rule("/<int:product_id>", methods=["GET"], view_func=get_product_by_id)
product_bp.add_url_rule("/<int:product_id>", methods=["PUT"], view_func=update_product)
product_bp.add_url_rule("/<int:product_id>", methods=["DELETE"], view_func=delete_product)
