from flask import Flask
from app.config import Config


def create_app():
    """Application factory function"""
    app = Flask(__name__)
    
    # Load configuration
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['DEBUG'] = Config.DEBUG
    
    # Load config from YAML
    Config.load_from_yaml()
    
    # Register blueprints
    from app.my_project.route import (
        role_bp, user_bp, category_bp, subcategory_bp,
        product_bp, product_attribute_bp, product_image_bp,
        review_bp, order_bp, order_item_bp, payment_bp
    )
    
    app.register_blueprint(role_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(subcategory_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(product_attribute_bp)
    app.register_blueprint(product_image_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(order_item_bp)
    app.register_blueprint(payment_bp)
    
    # Root route
    @app.route('/')
    def index():
        return {
            'message': 'E-Commerce API',
            'version': '1.0.0',
            'endpoints': {
                'roles': '/api/roles',
                'users': '/api/users',
                'categories': '/api/categories',
                'subcategories': '/api/subcategories',
                'products': '/api/products',
                'product_attributes': '/api/product-attributes',
                'product_images': '/api/product-images',
                'reviews': '/api/reviews',
                'orders': '/api/orders',
                'order_items': '/api/order-items',
                'payments': '/api/payments'
            }
        }
    
    return app

