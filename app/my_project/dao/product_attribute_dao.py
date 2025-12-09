from app.config import Config
from app.my_project.domain import ProductAttribute


class ProductAttributeDAO:
    """Data Access Object for ProductAttribute entity"""

    @staticmethod
    def get_all():
        """Get all product attributes"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT attribute_id, product_id, attribute_name, attribute_value 
                FROM product_attributes
            """)
            rows = cursor.fetchall()
            return [ProductAttribute.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(attribute_id):
        """Get product attribute by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT attribute_id, product_id, attribute_name, attribute_value 
                FROM product_attributes WHERE attribute_id = %s
            """, (attribute_id,))
            row = cursor.fetchone()
            return ProductAttribute.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_product(product_id):
        """Get all attributes for a product"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT attribute_id, product_id, attribute_name, attribute_value 
                FROM product_attributes WHERE product_id = %s
            """, (product_id,))
            rows = cursor.fetchall()
            return [ProductAttribute.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(attribute):
        """Create a new product attribute"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO product_attributes (product_id, attribute_name, attribute_value) 
                VALUES (%s, %s, %s)
            """, (attribute.product_id, attribute.attribute_name, attribute.attribute_value))
            connection.commit()
            attribute.attribute_id = cursor.lastrowid
            return attribute
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(attribute):
        """Update an existing product attribute"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE product_attributes 
                SET product_id = %s, attribute_name = %s, attribute_value = %s 
                WHERE attribute_id = %s
            """, (attribute.product_id, attribute.attribute_name, 
                  attribute.attribute_value, attribute.attribute_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(attribute_id):
        """Delete a product attribute by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM product_attributes WHERE attribute_id = %s", (attribute_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

