from flask import request, jsonify
from schemas.order_schema import order_schema, orders_schema, track_order_schema
from marshmallow import ValidationError
from services import order_service
# from caching import cache
# from auth import token_auth

# @token_auth.login_required
def create_order():
    try:
        raw_data = request.json
        # logged_in_user = token_auth.current_user()
        # raw_data['customer_id'] = logged_in_user.id
        order_data = order_schema.load(raw_data)
        order_save = order_service.save(order_data)
        return order_schema.jsonify(order_save), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as err:
        return jsonify({'error': str(err)}), 400

# @cache.cached(timeout=60)
def get_all_orders():
    orders = order_service.find_all()
    return orders_schema.jsonify(orders)

def get_order_by_id(order_id):
    try:
        order = order_service.find_by_id(order_id)
        if order: return order_schema.jsonify(order), 200
        return jsonify({'message': 'Order not found'}), 404
    except ValidationError as err: return jsonify(err.messages), 400
    except ValueError as err: return jsonify({'error': str(err)}), 400

def track_order_by_id(order_id):
    try:
        order = order_service.find_by_id(order_id)
        if order: return track_order_schema.jsonify(order), 200
        return jsonify({'message': 'Order not found'}), 404
    except ValidationError as err: return jsonify(err.messages), 400
    except ValueError as err: return jsonify({'error': str(err)}), 400