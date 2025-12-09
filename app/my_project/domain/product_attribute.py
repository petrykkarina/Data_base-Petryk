class ProductAttribute:
    """Domain model for ProductAttribute entity"""
    
    def __init__(self, attribute_id=None, product_id=None, 
                 attribute_name=None, attribute_value=None):
        self.attribute_id = attribute_id
        self.product_id = product_id
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value

    def to_dict(self):
        """Convert ProductAttribute to dictionary (DTO)"""
        return {
            'attribute_id': self.attribute_id,
            'product_id': self.product_id,
            'attribute_name': self.attribute_name,
            'attribute_value': self.attribute_value
        }

    @staticmethod
    def from_dict(data):
        """Create ProductAttribute from dictionary"""
        return ProductAttribute(
            attribute_id=data.get('attribute_id'),
            product_id=data.get('product_id'),
            attribute_name=data.get('attribute_name'),
            attribute_value=data.get('attribute_value')
        )

    @staticmethod
    def from_db_row(row):
        """Create ProductAttribute from database row tuple"""
        if row is None:
            return None
        return ProductAttribute(
            attribute_id=row[0],
            product_id=row[1],
            attribute_name=row[2],
            attribute_value=row[3]
        )

    def __repr__(self):
        return f"ProductAttribute(attribute_id={self.attribute_id}, attribute_name='{self.attribute_name}')"

