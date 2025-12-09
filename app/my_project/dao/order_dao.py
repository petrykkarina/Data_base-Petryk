from app.config import Config
from app.my_project.domain import Order


class OrderDAO:
    """Data Access Object for Order entity"""

    @staticmethod
    def get_all():
        """Get all orders"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT order_id, user_id, order_date, status, total 
                FROM orders
            """)
            rows = cursor.fetchall()
            return [Order.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(order_id):
        """Get order by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT order_id, user_id, order_date, status, total 
                FROM orders WHERE order_id = %s
            """, (order_id,))
            row = cursor.fetchone()
            return Order.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_user(user_id):
        """Get all orders for a user"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT order_id, user_id, order_date, status, total 
                FROM orders WHERE user_id = %s
            """, (user_id,))
            rows = cursor.fetchall()
            return [Order.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_status(status):
        """Get all orders with a specific status"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT order_id, user_id, order_date, status, total 
                FROM orders WHERE status = %s
            """, (status,))
            rows = cursor.fetchall()
            return [Order.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(order):
        """Create a new order"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO orders (user_id, order_date, status, total)
                VALUES (%s, NOW(), %s, %s)
            """, (order.user_id, order.status, order.total))
            connection.commit()
            order.order_id = cursor.lastrowid
            return order
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(order):
        """Update an existing order"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE orders 
                SET status = %s, total = %s 
                WHERE order_id = %s
            """, (order.status, order.total, order.order_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(order_id):
        """Delete an order by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

