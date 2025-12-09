class OrderItem:
    """Domain model for OrderItem entity"""
    
    def __init__(self, order_item_id=None, order_id=None, product_id=None,
                 quantity=None, price=None):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """Convert OrderItem to dictionary (DTO)"""
        return {
            'order_item_id': self.order_item_id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': float(self.price) if self.price else None
        }

    @staticmethod
    def from_dict(data):
        """Create OrderItem from dictionary"""
        return OrderItem(
            order_item_id=data.get('order_item_id'),
            order_id=data.get('order_id'),
            product_id=data.get('product_id'),
            quantity=data.get('quantity'),
            price=data.get('price')
        )

    @staticmethod
    def from_db_row(row):
        """Create OrderItem from database row tuple"""
        if row is None:
            return None
        return OrderItem(
            order_item_id=row[0],
            order_id=row[1],
            product_id=row[2],
            quantity=row[3],
            price=row[4]
        )

    def __repr__(self):
        return f"OrderItem(order_item_id={self.order_item_id}, quantity={self.quantity})"

