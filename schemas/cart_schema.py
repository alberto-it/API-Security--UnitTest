from marshmallow import Schema, fields

class ShoppingCartItemSchema(Schema):
    customer_id = fields.Integer(dump_only=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)

class ShoppingCartSchema(Schema):
    items = fields.List(fields.Nested(ShoppingCartItemSchema), required=True)
