from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from database import db
from schemas import ma
from limiter import limiter
from caching import cache

from models.customer_model import Customer
from models.product_model import Product
from models.order_model import Order
from models.order_product import order_product
from models.cart_products import CartItem
from models.role import Role

from routes.customers_blueprint import customer_bp
from routes.products_blueprint import product_bp
from routes.orders_blueprint import order_bp
from routes.cart_blueprint import cart_bp
from routes.token_blueprint import token_bp

from dotenv import load_dotenv
load_dotenv()

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': 'CT E-Commerce'}
)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)
    CORS(app)

    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(token_bp, url_prefix='/token')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    limiter.limit("100 per day")(customer_bp)
    limiter.limit("100 per day")(product_bp)
    limiter.limit("100 per day")(order_bp)
    limiter.limit("100 per day")(cart_bp)

    return app

if __name__ == "__main__":
    app = create_app('DevelopmentConfig')
    with app.app_context(): db.create_all()
    app.run(debug=True)