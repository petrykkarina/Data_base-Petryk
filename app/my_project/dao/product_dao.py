from app.config import Config
from app.my_project.domain import Product


class ProductDAO:
    """Data Access Object for Product entity"""

    @staticmethod
    def get_all():
        """Get all products"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT product_id, subcategory_id, name, description, price, stock, created_at 
                FROM products
            """)
            rows = cursor.fetchall()
            return [Product.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(product_id):
        """Get product by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT product_id, subcategory_id, name, description, price, stock, created_at 
                FROM products WHERE product_id = %s
            """, (product_id,))
            row = cursor.fetchone()
            return Product.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_subcategory(subcategory_id):
        """Get all products in a subcategory"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT product_id, subcategory_id, name, description, price, stock, created_at 
                FROM products WHERE subcategory_id = %s
            """, (subcategory_id,))
            rows = cursor.fetchall()
            return [Product.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(product):
        """Create a new product"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO products (subcategory_id, name, description, price, stock, created_at)
                VALUES (%s, %s, %s, %s, %s, NOW())
            """, (product.subcategory_id, product.name, product.description, 
                  product.price, product.stock))
            connection.commit()
            product.product_id = cursor.lastrowid
            return product
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(product):
        """Update an existing product"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE products 
                SET subcategory_id = %s, name = %s, description = %s, price = %s, stock = %s
                WHERE product_id = %s
            """, (product.subcategory_id, product.name, product.description, 
                  product.price, product.stock, product.product_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(product_id):
        """Delete a product by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

