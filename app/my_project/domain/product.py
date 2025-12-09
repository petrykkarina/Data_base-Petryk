class Product:
    """Domain model for Product entity"""
    
    def __init__(self, product_id=None, subcategory_id=None, name=None,
                 description=None, price=None, stock=None, created_at=None):
        self.product_id = product_id
        self.subcategory_id = subcategory_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.created_at = created_at

    def to_dict(self):
        """Convert Product to dictionary (DTO)"""
        return {
            'product_id': self.product_id,
            'subcategory_id': self.subcategory_id,
            'name': self.name,
            'description': self.description,
            'price': float(self.price) if self.price else None,
            'stock': self.stock,
            'created_at': str(self.created_at) if self.created_at else None
        }

    @staticmethod
    def from_dict(data):
        """Create Product from dictionary"""
        return Product(
            product_id=data.get('product_id'),
            subcategory_id=data.get('subcategory_id'),
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            stock=data.get('stock'),
            created_at=data.get('created_at')
        )

    @staticmethod
    def from_db_row(row):
        """Create Product from database row tuple"""
        if row is None:
            return None
        return Product(
            product_id=row[0],
            subcategory_id=row[1],
            name=row[2],
            description=row[3],
            price=row[4],
            stock=row[5],
            created_at=row[6]
        )

    def __repr__(self):
        return f"Product(product_id={self.product_id}, name='{self.name}')"

