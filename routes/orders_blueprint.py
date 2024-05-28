from flask import Blueprint
from controllers.order_controller import (
    create_order,  
    get_all_orders,
    get_order_by_id,
    track_order_by_id
)

order_bp = Blueprint("order_bp", __name__)

order_bp.add_url_rule("/", methods=["POST"], view_func=create_order)
order_bp.add_url_rule("/", methods=["GET"], view_func=get_all_orders)
order_bp.add_url_rule("/<int:order_id>", methods=["GET"], view_func=get_order_by_id)
order_bp.add_url_rule("/<int:order_id>/track", methods=["GET"], view_func=track_order_by_id)
