from marshmallow import fields
from schemas import ma

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False) 
    name = fields.String(required=True)
    price = fields.Float(required=True)

    class Meta:
        fields = ("id", "name", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True) 

class ProductIdSchema(ma.Schema):
    id = fields.Integer(required=True)  
    name = fields.String(required=False)
    price = fields.String(required=False)

class ProductUpdateSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=False)
    price = fields.Float(required=False)

product_update_schema = ProductUpdateSchema()