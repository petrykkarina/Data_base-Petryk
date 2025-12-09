from app.config import Config
from app.my_project.domain import Payment


class PaymentDAO:
    """Data Access Object for Payment entity"""

    @staticmethod
    def get_all():
        """Get all payments"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT payment_id, order_id, payment_method, payment_date, amount 
                FROM payments
            """)
            rows = cursor.fetchall()
            return [Payment.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(payment_id):
        """Get payment by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT payment_id, order_id, payment_method, payment_date, amount 
                FROM payments WHERE payment_id = %s
            """, (payment_id,))
            row = cursor.fetchone()
            return Payment.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_order(order_id):
        """Get payment for an order"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT payment_id, order_id, payment_method, payment_date, amount 
                FROM payments WHERE order_id = %s
            """, (order_id,))
            row = cursor.fetchone()
            return Payment.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(payment):
        """Create a new payment"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO payments (order_id, payment_method, payment_date, amount)
                VALUES (%s, %s, NOW(), %s)
            """, (payment.order_id, payment.payment_method, payment.amount))
            connection.commit()
            payment.payment_id = cursor.lastrowid
            return payment
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(payment):
        """Update an existing payment"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE payments 
                SET payment_method = %s, amount = %s 
                WHERE payment_id = %s
            """, (payment.payment_method, payment.amount, payment.payment_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(payment_id):
        """Delete a payment by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM payments WHERE payment_id = %s", (payment_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

