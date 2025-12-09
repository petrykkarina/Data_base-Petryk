class Subcategory:
    """Domain model for Subcategory entity"""
    
    def __init__(self, subcategory_id=None, category_id=None, 
                 subcategory_name=None, description=None):
        self.subcategory_id = subcategory_id
        self.category_id = category_id
        self.subcategory_name = subcategory_name
        self.description = description

    def to_dict(self):
        """Convert Subcategory to dictionary (DTO)"""
        return {
            'subcategory_id': self.subcategory_id,
            'category_id': self.category_id,
            'subcategory_name': self.subcategory_name,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        """Create Subcategory from dictionary"""
        return Subcategory(
            subcategory_id=data.get('subcategory_id'),
            category_id=data.get('category_id'),
            subcategory_name=data.get('subcategory_name'),
            description=data.get('description')
        )

    @staticmethod
    def from_db_row(row):
        """Create Subcategory from database row tuple"""
        if row is None:
            return None
        return Subcategory(
            subcategory_id=row[0],
            category_id=row[1],
            subcategory_name=row[2],
            description=row[3]
        )

    def __repr__(self):
        return f"Subcategory(subcategory_id={self.subcategory_id}, subcategory_name='{self.subcategory_name}')"

