from app.config import Config
from app.my_project.domain import OrderItem


class OrderItemDAO:
    """Data Access Object for OrderItem entity"""

    @staticmethod
    def get_all():
        """Get all order items"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT order_item_id, order_id, product_id, quantity, price 
                FROM order_items
            """)
            rows = cursor.fetchall()
            return [OrderItem.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(order_item_id):
        """Get order item by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT order_item_id, order_id, product_id, quantity, price 
                FROM order_items WHERE order_item_id = %s
            """, (order_item_id,))
            row = cursor.fetchone()
            return OrderItem.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_order(order_id):
        """Get all items for an order"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT order_item_id, order_id, product_id, quantity, price 
                FROM order_items WHERE order_id = %s
            """, (order_id,))
            rows = cursor.fetchall()
            return [OrderItem.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(order_item):
        """Create a new order item"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO order_items (order_id, product_id, quantity, price)
                VALUES (%s, %s, %s, %s)
            """, (order_item.order_id, order_item.product_id, 
                  order_item.quantity, order_item.price))
            connection.commit()
            order_item.order_item_id = cursor.lastrowid
            return order_item
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(order_item):
        """Update an existing order item"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE order_items 
                SET quantity = %s, price = %s 
                WHERE order_item_id = %s
            """, (order_item.quantity, order_item.price, order_item.order_item_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(order_item_id):
        """Delete an order item by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM order_items WHERE order_item_id = %s", (order_item_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

