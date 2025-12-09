class Order:
    """Domain model for Order entity"""
    
    def __init__(self, order_id=None, user_id=None, order_date=None,
                 status=None, total=None):
        self.order_id = order_id
        self.user_id = user_id
        self.order_date = order_date
        self.status = status
        self.total = total

    def to_dict(self):
        """Convert Order to dictionary (DTO)"""
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'order_date': str(self.order_date) if self.order_date else None,
            'status': self.status,
            'total': float(self.total) if self.total else None
        }

    @staticmethod
    def from_dict(data):
        """Create Order from dictionary"""
        return Order(
            order_id=data.get('order_id'),
            user_id=data.get('user_id'),
            order_date=data.get('order_date'),
            status=data.get('status'),
            total=data.get('total')
        )

    @staticmethod
    def from_db_row(row):
        """Create Order from database row tuple"""
        if row is None:
            return None
        return Order(
            order_id=row[0],
            user_id=row[1],
            order_date=row[2],
            status=row[3],
            total=row[4]
        )

    def __repr__(self):
        return f"Order(order_id={self.order_id}, status='{self.status}')"

