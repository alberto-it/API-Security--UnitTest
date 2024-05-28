from flask import request, jsonify
from schemas.customer_schema import (
    customer_input_schema, 
    customer_output_schema, 
    customers_schema, 
    customer_login_schema,
    customer_update_schema)
from services import customer_service
from marshmallow import ValidationError
from caching import cache

def generate_token():
    try:
        customer = customer_login_schema.load(request.json)
        token = customer_service.get_token(customer['username'], customer['password'])
        if token: return jsonify({"status": "success", "message": "You have successfully logged in", "token": token}), 200
        return jsonify({"status": "error", "message": "Username and/or password is incorrect"}), 401
    except ValidationError as err: return jsonify(err.messages), 400

def save_customer():
    try:
        customer_data = customer_input_schema.load(request.json)
        customer_save = customer_service.save(customer_data)
        return customer_output_schema.jsonify(customer_save), 201
    except ValidationError as err: return jsonify(err.messages), 400
    except ValueError as err: return jsonify({"error": str(err)}), 400

@cache.cached(timeout=60)
def find_all_customers():
    args = request.args
    page = args.get('page', 1, type=int)
    per_page = args.get('per_page', 10, type=int)
    customers = customer_service.find_all(page, per_page)
    return customers_schema.jsonify(customers), 200

def find_customer_by_id(customer_id):
    customer = customer_service.get_customer(customer_id)
    if customer: return customer_output_schema.jsonify(customer), 200
    return jsonify({"message": "Customer not found"}), 404

def update_customer(customer_id):
    try:
        customer = customer_service.get_customer(customer_id)
        if customer is None: return jsonify({"message": "Customer not found"}), 404
        customer = customer_update_schema.load(request.json)
        updated_customer = customer_service.update_customer(customer_id, customer)
        return customer_output_schema.jsonify(updated_customer), 200
    except ValidationError as err: return jsonify(err.messages), 400
    except ValueError as err: return jsonify({"error": str(err)}), 400

def delete_customer(customer_id):
    customer_deleted = customer_service.delete_customer(customer_id)
    if customer_deleted: return jsonify({"message": "Customer deleted successfully"}), 204
    return jsonify({"message": "Customer not found"}), 404