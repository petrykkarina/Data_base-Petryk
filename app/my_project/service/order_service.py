from app.my_project.dao import OrderDAO
from app.my_project.domain import Order


class OrderService:
    """Service layer for Order entity with business logic"""

    VALID_STATUSES = ['pending', 'processing', 'shipped', 'delivered', 'cancelled']

    @staticmethod
    def get_all():
        """Get all orders"""
        orders = OrderDAO.get_all()
        return [order.to_dict() for order in orders]

    @staticmethod
    def get_by_id(order_id):
        """Get order by ID"""
        order = OrderDAO.get_by_id(order_id)
        if order is None:
            return None
        return order.to_dict()

    @staticmethod
    def get_by_user(user_id):
        """Get all orders for a user"""
        orders = OrderDAO.get_by_user(user_id)
        return [order.to_dict() for order in orders]

    @staticmethod
    def get_by_status(status):
        """Get all orders with a specific status"""
        orders = OrderDAO.get_by_status(status)
        return [order.to_dict() for order in orders]

    @staticmethod
    def create(data):
        """Create a new order"""
        if not data.get('user_id'):
            raise ValueError("User ID is required")
        
        status = data.get('status', 'pending')
        if status not in OrderService.VALID_STATUSES:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(OrderService.VALID_STATUSES)}")
        
        order = Order(
            user_id=data['user_id'],
            status=status,
            total=data.get('total', 0)
        )
        
        created_order = OrderDAO.create(order)
        return created_order.to_dict()

    @staticmethod
    def update(order_id, data):
        """Update an existing order"""
        existing_order = OrderDAO.get_by_id(order_id)
        if existing_order is None:
            return None
        
        if data.get('status'):
            if data['status'] not in OrderService.VALID_STATUSES:
                raise ValueError(f"Invalid status. Must be one of: {', '.join(OrderService.VALID_STATUSES)}")
            existing_order.status = data['status']
        
        existing_order.total = data.get('total', existing_order.total)
        
        success = OrderDAO.update(existing_order)
        if success:
            return existing_order.to_dict()
        return None

    @staticmethod
    def delete(order_id):
        """Delete an order by ID"""
        existing_order = OrderDAO.get_by_id(order_id)
        if existing_order is None:
            return False
        
        return OrderDAO.delete(order_id)

