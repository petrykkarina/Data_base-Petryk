from app.my_project.dao import OrderItemDAO
from app.my_project.domain import OrderItem


class OrderItemService:
    """Service layer for OrderItem entity with business logic"""

    @staticmethod
    def get_all():
        """Get all order items"""
        order_items = OrderItemDAO.get_all()
        return [order_item.to_dict() for order_item in order_items]

    @staticmethod
    def get_by_id(order_item_id):
        """Get order item by ID"""
        order_item = OrderItemDAO.get_by_id(order_item_id)
        if order_item is None:
            return None
        return order_item.to_dict()

    @staticmethod
    def get_by_order(order_id):
        """Get all items for an order"""
        order_items = OrderItemDAO.get_by_order(order_id)
        return [order_item.to_dict() for order_item in order_items]

    @staticmethod
    def create(data):
        """Create a new order item"""
        if not data.get('order_id'):
            raise ValueError("Order ID is required")
        if not data.get('product_id'):
            raise ValueError("Product ID is required")
        if not data.get('quantity'):
            raise ValueError("Quantity is required")
        if not data.get('price'):
            raise ValueError("Price is required")
        
        if data['quantity'] <= 0:
            raise ValueError("Quantity must be greater than 0")
        if data['price'] < 0:
            raise ValueError("Price cannot be negative")
        
        order_item = OrderItem.from_dict(data)
        created_order_item = OrderItemDAO.create(order_item)
        return created_order_item.to_dict()

    @staticmethod
    def update(order_item_id, data):
        """Update an existing order item"""
        existing_order_item = OrderItemDAO.get_by_id(order_item_id)
        if existing_order_item is None:
            return None
        
        if data.get('quantity'):
            if data['quantity'] <= 0:
                raise ValueError("Quantity must be greater than 0")
            existing_order_item.quantity = data['quantity']
        
        if data.get('price'):
            if data['price'] < 0:
                raise ValueError("Price cannot be negative")
            existing_order_item.price = data['price']
        
        success = OrderItemDAO.update(existing_order_item)
        if success:
            return existing_order_item.to_dict()
        return None

    @staticmethod
    def delete(order_item_id):
        """Delete an order item by ID"""
        existing_order_item = OrderItemDAO.get_by_id(order_item_id)
        if existing_order_item is None:
            return False
        
        return OrderItemDAO.delete(order_item_id)

