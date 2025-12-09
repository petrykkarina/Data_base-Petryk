from flask import Blueprint

# Create blueprints for each entity
role_bp = Blueprint('roles', __name__, url_prefix='/api/roles')
user_bp = Blueprint('users', __name__, url_prefix='/api/users')
category_bp = Blueprint('categories', __name__, url_prefix='/api/categories')
subcategory_bp = Blueprint('subcategories', __name__, url_prefix='/api/subcategories')
product_bp = Blueprint('products', __name__, url_prefix='/api/products')
product_attribute_bp = Blueprint('product_attributes', __name__, url_prefix='/api/product-attributes')
product_image_bp = Blueprint('product_images', __name__, url_prefix='/api/product-images')
review_bp = Blueprint('reviews', __name__, url_prefix='/api/reviews')
order_bp = Blueprint('orders', __name__, url_prefix='/api/orders')
order_item_bp = Blueprint('order_items', __name__, url_prefix='/api/order-items')
payment_bp = Blueprint('payments', __name__, url_prefix='/api/payments')

# Import routes to register them
from . import role_route
from . import user_route
from . import category_route
from . import subcategory_route
from . import product_route
from . import product_attribute_route
from . import product_image_route
from . import review_route
from . import order_route
from . import order_item_route
from . import payment_route

