from flask_httpauth import HTTPTokenAuth
from utils.util import decode_token
from services import customer_service

token_auth = HTTPTokenAuth()

@token_auth.verify_token
def verify(token):
    customer_id = decode_token(token)
    if customer_id: return customer_service.get_customer(customer_id)
    
@token_auth.error_handler
def handle_error(status_code):
    return {"error": "Invalid Token. Please try again"}, status_code

@token_auth.get_user_roles
def get_roles(customer): return [customer.role.role_name]