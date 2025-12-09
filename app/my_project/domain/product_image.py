class ProductImage:
    """Domain model for ProductImage entity"""
    
    def __init__(self, image_id=None, product_id=None, 
                 image_url=None, is_main=None):
        self.image_id = image_id
        self.product_id = product_id
        self.image_url = image_url
        self.is_main = is_main

    def to_dict(self):
        """Convert ProductImage to dictionary (DTO)"""
        return {
            'image_id': self.image_id,
            'product_id': self.product_id,
            'image_url': self.image_url,
            'is_main': bool(self.is_main) if self.is_main is not None else None
        }

    @staticmethod
    def from_dict(data):
        """Create ProductImage from dictionary"""
        return ProductImage(
            image_id=data.get('image_id'),
            product_id=data.get('product_id'),
            image_url=data.get('image_url'),
            is_main=data.get('is_main')
        )

    @staticmethod
    def from_db_row(row):
        """Create ProductImage from database row tuple"""
        if row is None:
            return None
        return ProductImage(
            image_id=row[0],
            product_id=row[1],
            image_url=row[2],
            is_main=row[3]
        )

    def __repr__(self):
        return f"ProductImage(image_id={self.image_id}, image_url='{self.image_url}')"

