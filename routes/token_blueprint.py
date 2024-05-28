from flask import Blueprint
from controllers.customer_controller import generate_token

token_bp = Blueprint('token_bp', __name__)

token_bp.add_url_rule("/", methods=["POST"], view_func=generate_token)