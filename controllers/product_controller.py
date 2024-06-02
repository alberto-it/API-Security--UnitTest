from flask import request, jsonify
from schemas.product_schema import product_schema, products_schema, product_update_schema
from services import product_service
from marshmallow import ValidationError
from caching import cache
# from auth import token_auth

# @token_auth.login_required(role='admin')
def create_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    product_save = product_service.save(product_data)
    if product_save is not None: return product_schema.jsonify(product_save), 201
    return jsonify({"message": "Fallback method error activated", "body": product_data}), 400

@cache.cached(timeout=60)
def get_products():
    args = request.args
    page = args.get('page', 1, type=int)
    per_page = args.get('per_page', 10, type=int)
    search_term = args.get('search')
    products = product_service.find(page, per_page, search_term)
    return products_schema.jsonify(products), 200


def get_product_by_id(product_id):
    product = product_service.find_by_id(product_id)
    if product: return product_schema.jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

def update_product(product_id):
    try:
        product = product_service.get_product(product_id)
        if product is None: return jsonify({"message": "Product not found"}), 404
        product = product_update_schema.load(request.json)
        updated_product = product_service.update_product(product_id, product)
        return product_schema.jsonify(updated_product), 200
    except ValidationError as err: return jsonify(err.messages), 400
    except ValueError as err: return jsonify({"error": str(err)}), 400

def delete_product(product_id):
    product_deleted = product_service.delete_product(product_id)
    if product_deleted: return jsonify({"message": "Product deleted successfully"}), 204
    return jsonify({"message": "Product not found"}), 404