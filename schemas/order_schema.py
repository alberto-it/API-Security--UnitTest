from marshmallow import fields
from schemas import ma
from schemas.product_schema import ProductIdSchema


class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_dt = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.Nested(ProductIdSchema, required=True, many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class TrackOrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_dt = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    status = fields.String(required=False) 
    expected_dt = fields.Date(required=False) 

track_order_schema = TrackOrderSchema()