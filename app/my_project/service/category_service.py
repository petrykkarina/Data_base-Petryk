from app.my_project.dao import CategoryDAO
from app.my_project.domain import Category


class CategoryService:
    """Service layer for Category entity with business logic"""

    @staticmethod
    def get_all():
        """Get all categories"""
        categories = CategoryDAO.get_all()
        return [category.to_dict() for category in categories]

    @staticmethod
    def get_by_id(category_id):
        """Get category by ID"""
        category = CategoryDAO.get_by_id(category_id)
        if category is None:
            return None
        return category.to_dict()

    @staticmethod
    def create(data):
        """Create a new category"""
        if not data.get('category_name'):
            raise ValueError("Category name is required")
        
        category = Category.from_dict(data)
        created_category = CategoryDAO.create(category)
        return created_category.to_dict()

    @staticmethod
    def update(category_id, data):
        """Update an existing category"""
        existing_category = CategoryDAO.get_by_id(category_id)
        if existing_category is None:
            return None
        
        existing_category.category_name = data.get('category_name', existing_category.category_name)
        existing_category.description = data.get('description', existing_category.description)
        
        success = CategoryDAO.update(existing_category)
        if success:
            return existing_category.to_dict()
        return None

    @staticmethod
    def delete(category_id):
        """Delete a category by ID"""
        existing_category = CategoryDAO.get_by_id(category_id)
        if existing_category is None:
            return False
        
        return CategoryDAO.delete(category_id)

