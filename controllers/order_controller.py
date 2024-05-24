from flask import request, jsonify
from schemas.order_schema import order_schema, orders_schema
from marshmallow import ValidationError
from services import order_service
from auth import token_auth


@token_auth.login_required
def save():
    try:
        raw_data = request.json
        logged_in_user = token_auth.current_user()
        raw_data['customer_id'] = logged_in_user.id
        order_data = order_schema.load(raw_data)
        order_save = order_service.save(order_data)
        return order_schema.jsonify(order_save), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as err:
        return jsonify({'error': str(err)}), 400

def find_all():
    orders = order_service.find_all()
    return orders_schema.jsonify(orders)