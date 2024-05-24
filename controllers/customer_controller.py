from flask import request, jsonify
from schemas.customer_schema import customer_input_schema, customer_output_schema, customers_schema, customer_login_schema
from services import customer_service
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        customer_data = customer_input_schema.load(request.json)
        customer_save = customer_service.save(customer_data)
        return customer_output_schema.jsonify(customer_save), 201
    except ValidationError as err: return jsonify(err.messages), 400
    except ValueError as err: return jsonify({"error": str(err)}), 400

@cache.cached(timeout=60)
def find_all():
    customers = customer_service.find_all()
    return customers_schema.jsonify(customers), 200

def get_token():
    try:
        customer_data = customer_login_schema.load(request.json)
        token = customer_service.get_token(customer_data['username'], customer_data['password'])
        if token:
            resp = {
                "status": "success",
                "message": "You have successfully authenticated yourself",
                "token": token
            }
            return jsonify(resp), 200
        else:
            resp = {
                "status": "error",
                "message": "Username and/or password is incorrect"
            }
            return jsonify(resp), 401
    except ValidationError as err: return jsonify(err.messages), 400