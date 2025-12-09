from app.my_project.dao import ProductImageDAO
from app.my_project.domain import ProductImage


class ProductImageService:
    """Service layer for ProductImage entity with business logic"""

    @staticmethod
    def get_all():
        """Get all product images"""
        images = ProductImageDAO.get_all()
        return [image.to_dict() for image in images]

    @staticmethod
    def get_by_id(image_id):
        """Get product image by ID"""
        image = ProductImageDAO.get_by_id(image_id)
        if image is None:
            return None
        return image.to_dict()

    @staticmethod
    def get_by_product(product_id):
        """Get all images for a product"""
        images = ProductImageDAO.get_by_product(product_id)
        return [image.to_dict() for image in images]

    @staticmethod
    def get_main_image(product_id):
        """Get main image for a product"""
        image = ProductImageDAO.get_main_image(product_id)
        if image is None:
            return None
        return image.to_dict()

    @staticmethod
    def create(data):
        """Create a new product image"""
        if not data.get('product_id'):
            raise ValueError("Product ID is required")
        if not data.get('image_url'):
            raise ValueError("Image URL is required")
        
        image = ProductImage.from_dict(data)
        created_image = ProductImageDAO.create(image)
        return created_image.to_dict()

    @staticmethod
    def update(image_id, data):
        """Update an existing product image"""
        existing_image = ProductImageDAO.get_by_id(image_id)
        if existing_image is None:
            return None
        
        existing_image.image_url = data.get('image_url', existing_image.image_url)
        existing_image.is_main = data.get('is_main', existing_image.is_main)
        existing_image.product_id = data.get('product_id', existing_image.product_id)
        
        success = ProductImageDAO.update(existing_image)
        if success:
            return existing_image.to_dict()
        return None

    @staticmethod
    def delete(image_id):
        """Delete a product image by ID"""
        existing_image = ProductImageDAO.get_by_id(image_id)
        if existing_image is None:
            return False
        
        return ProductImageDAO.delete(image_id)

