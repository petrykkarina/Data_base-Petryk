from app.my_project.dao import SubcategoryDAO
from app.my_project.domain import Subcategory


class SubcategoryService:
    """Service layer for Subcategory entity with business logic"""

    @staticmethod
    def get_all():
        """Get all subcategories"""
        subcategories = SubcategoryDAO.get_all()
        return [subcategory.to_dict() for subcategory in subcategories]

    @staticmethod
    def get_by_id(subcategory_id):
        """Get subcategory by ID"""
        subcategory = SubcategoryDAO.get_by_id(subcategory_id)
        if subcategory is None:
            return None
        return subcategory.to_dict()

    @staticmethod
    def get_by_category(category_id):
        """Get all subcategories for a category"""
        subcategories = SubcategoryDAO.get_by_category(category_id)
        return [subcategory.to_dict() for subcategory in subcategories]

    @staticmethod
    def create(data):
        """Create a new subcategory"""
        if not data.get('subcategory_name'):
            raise ValueError("Subcategory name is required")
        if not data.get('category_id'):
            raise ValueError("Category ID is required")
        
        subcategory = Subcategory.from_dict(data)
        created_subcategory = SubcategoryDAO.create(subcategory)
        return created_subcategory.to_dict()

    @staticmethod
    def update(subcategory_id, data):
        """Update an existing subcategory"""
        existing_subcategory = SubcategoryDAO.get_by_id(subcategory_id)
        if existing_subcategory is None:
            return None
        
        existing_subcategory.subcategory_name = data.get('subcategory_name', existing_subcategory.subcategory_name)
        existing_subcategory.description = data.get('description', existing_subcategory.description)
        existing_subcategory.category_id = data.get('category_id', existing_subcategory.category_id)
        
        success = SubcategoryDAO.update(existing_subcategory)
        if success:
            return existing_subcategory.to_dict()
        return None

    @staticmethod
    def delete(subcategory_id):
        """Delete a subcategory by ID"""
        existing_subcategory = SubcategoryDAO.get_by_id(subcategory_id)
        if existing_subcategory is None:
            return False
        
        return SubcategoryDAO.delete(subcategory_id)

