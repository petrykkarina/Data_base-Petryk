from app.my_project.dao import ProductDAO
from app.my_project.domain import Product


class ProductService:
    """Service layer for Product entity with business logic"""

    @staticmethod
    def get_all():
        """Get all products"""
        products = ProductDAO.get_all()
        return [product.to_dict() for product in products]

    @staticmethod
    def get_by_id(product_id):
        """Get product by ID"""
        product = ProductDAO.get_by_id(product_id)
        if product is None:
            return None
        return product.to_dict()

    @staticmethod
    def get_by_subcategory(subcategory_id):
        """Get all products in a subcategory"""
        products = ProductDAO.get_by_subcategory(subcategory_id)
        return [product.to_dict() for product in products]

    @staticmethod
    def create(data):
        """Create a new product"""
        if not data.get('name'):
            raise ValueError("Product name is required")
        if not data.get('price'):
            raise ValueError("Product price is required")
        if not data.get('subcategory_id'):
            raise ValueError("Subcategory ID is required")
        
        product = Product.from_dict(data)
        created_product = ProductDAO.create(product)
        return created_product.to_dict()

    @staticmethod
    def update(product_id, data):
        """Update an existing product"""
        existing_product = ProductDAO.get_by_id(product_id)
        if existing_product is None:
            return None
        
        existing_product.name = data.get('name', existing_product.name)
        existing_product.description = data.get('description', existing_product.description)
        existing_product.price = data.get('price', existing_product.price)
        existing_product.stock = data.get('stock', existing_product.stock)
        existing_product.subcategory_id = data.get('subcategory_id', existing_product.subcategory_id)
        
        success = ProductDAO.update(existing_product)
        if success:
            return existing_product.to_dict()
        return None

    @staticmethod
    def delete(product_id):
        """Delete a product by ID"""
        existing_product = ProductDAO.get_by_id(product_id)
        if existing_product is None:
            return False
        
        return ProductDAO.delete(product_id)

