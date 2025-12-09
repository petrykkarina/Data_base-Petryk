from app.my_project.dao import ProductAttributeDAO
from app.my_project.domain import ProductAttribute


class ProductAttributeService:
    """Service layer for ProductAttribute entity with business logic"""

    @staticmethod
    def get_all():
        """Get all product attributes"""
        attributes = ProductAttributeDAO.get_all()
        return [attribute.to_dict() for attribute in attributes]

    @staticmethod
    def get_by_id(attribute_id):
        """Get product attribute by ID"""
        attribute = ProductAttributeDAO.get_by_id(attribute_id)
        if attribute is None:
            return None
        return attribute.to_dict()

    @staticmethod
    def get_by_product(product_id):
        """Get all attributes for a product"""
        attributes = ProductAttributeDAO.get_by_product(product_id)
        return [attribute.to_dict() for attribute in attributes]

    @staticmethod
    def create(data):
        """Create a new product attribute"""
        if not data.get('product_id'):
            raise ValueError("Product ID is required")
        if not data.get('attribute_name'):
            raise ValueError("Attribute name is required")
        
        attribute = ProductAttribute.from_dict(data)
        created_attribute = ProductAttributeDAO.create(attribute)
        return created_attribute.to_dict()

    @staticmethod
    def update(attribute_id, data):
        """Update an existing product attribute"""
        existing_attribute = ProductAttributeDAO.get_by_id(attribute_id)
        if existing_attribute is None:
            return None
        
        existing_attribute.attribute_name = data.get('attribute_name', existing_attribute.attribute_name)
        existing_attribute.attribute_value = data.get('attribute_value', existing_attribute.attribute_value)
        existing_attribute.product_id = data.get('product_id', existing_attribute.product_id)
        
        success = ProductAttributeDAO.update(existing_attribute)
        if success:
            return existing_attribute.to_dict()
        return None

    @staticmethod
    def delete(attribute_id):
        """Delete a product attribute by ID"""
        existing_attribute = ProductAttributeDAO.get_by_id(attribute_id)
        if existing_attribute is None:
            return False
        
        return ProductAttributeDAO.delete(attribute_id)

