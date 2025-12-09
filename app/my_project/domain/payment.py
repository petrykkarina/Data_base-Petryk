class Payment:
    """Domain model for Payment entity"""
    
    def __init__(self, payment_id=None, order_id=None, payment_method=None,
                 payment_date=None, amount=None):
        self.payment_id = payment_id
        self.order_id = order_id
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.amount = amount

    def to_dict(self):
        """Convert Payment to dictionary (DTO)"""
        return {
            'payment_id': self.payment_id,
            'order_id': self.order_id,
            'payment_method': self.payment_method,
            'payment_date': str(self.payment_date) if self.payment_date else None,
            'amount': float(self.amount) if self.amount else None
        }

    @staticmethod
    def from_dict(data):
        """Create Payment from dictionary"""
        return Payment(
            payment_id=data.get('payment_id'),
            order_id=data.get('order_id'),
            payment_method=data.get('payment_method'),
            payment_date=data.get('payment_date'),
            amount=data.get('amount')
        )

    @staticmethod
    def from_db_row(row):
        """Create Payment from database row tuple"""
        if row is None:
            return None
        return Payment(
            payment_id=row[0],
            order_id=row[1],
            payment_method=row[2],
            payment_date=row[3],
            amount=row[4]
        )

    def __repr__(self):
        return f"Payment(payment_id={self.payment_id}, amount={self.amount})"

