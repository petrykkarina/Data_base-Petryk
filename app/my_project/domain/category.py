class Category:
    """Domain model for Category entity"""
    
    def __init__(self, category_id=None, category_name=None, description=None):
        self.category_id = category_id
        self.category_name = category_name
        self.description = description

    def to_dict(self):
        """Convert Category to dictionary (DTO)"""
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        """Create Category from dictionary"""
        return Category(
            category_id=data.get('category_id'),
            category_name=data.get('category_name'),
            description=data.get('description')
        )

    @staticmethod
    def from_db_row(row):
        """Create Category from database row tuple"""
        if row is None:
            return None
        return Category(
            category_id=row[0],
            category_name=row[1],
            description=row[2]
        )

    def __repr__(self):
        return f"Category(category_id={self.category_id}, category_name='{self.category_name}')"

