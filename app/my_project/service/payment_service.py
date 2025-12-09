from app.my_project.dao import PaymentDAO
from app.my_project.domain import Payment


class PaymentService:
    """Service layer for Payment entity with business logic"""

    VALID_PAYMENT_METHODS = ['credit_card', 'debit_card', 'paypal', 'cash', 'bank_transfer']

    @staticmethod
    def get_all():
        """Get all payments"""
        payments = PaymentDAO.get_all()
        return [payment.to_dict() for payment in payments]

    @staticmethod
    def get_by_id(payment_id):
        """Get payment by ID"""
        payment = PaymentDAO.get_by_id(payment_id)
        if payment is None:
            return None
        return payment.to_dict()

    @staticmethod
    def get_by_order(order_id):
        """Get payment for an order"""
        payment = PaymentDAO.get_by_order(order_id)
        if payment is None:
            return None
        return payment.to_dict()

    @staticmethod
    def create(data):
        """Create a new payment"""
        if not data.get('order_id'):
            raise ValueError("Order ID is required")
        if not data.get('payment_method'):
            raise ValueError("Payment method is required")
        if not data.get('amount'):
            raise ValueError("Amount is required")
        
        payment_method = data['payment_method']
        if payment_method not in PaymentService.VALID_PAYMENT_METHODS:
            raise ValueError(f"Invalid payment method. Must be one of: {', '.join(PaymentService.VALID_PAYMENT_METHODS)}")
        
        if data['amount'] <= 0:
            raise ValueError("Amount must be greater than 0")
        
        payment = Payment.from_dict(data)
        created_payment = PaymentDAO.create(payment)
        return created_payment.to_dict()

    @staticmethod
    def update(payment_id, data):
        """Update an existing payment"""
        existing_payment = PaymentDAO.get_by_id(payment_id)
        if existing_payment is None:
            return None
        
        if data.get('payment_method'):
            if data['payment_method'] not in PaymentService.VALID_PAYMENT_METHODS:
                raise ValueError(f"Invalid payment method. Must be one of: {', '.join(PaymentService.VALID_PAYMENT_METHODS)}")
            existing_payment.payment_method = data['payment_method']
        
        if data.get('amount'):
            if data['amount'] <= 0:
                raise ValueError("Amount must be greater than 0")
            existing_payment.amount = data['amount']
        
        success = PaymentDAO.update(existing_payment)
        if success:
            return existing_payment.to_dict()
        return None

    @staticmethod
    def delete(payment_id):
        """Delete a payment by ID"""
        existing_payment = PaymentDAO.get_by_id(payment_id)
        if existing_payment is None:
            return False
        
        return PaymentDAO.delete(payment_id)

