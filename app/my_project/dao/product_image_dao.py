from app.config import Config
from app.my_project.domain import ProductImage


class ProductImageDAO:
    """Data Access Object for ProductImage entity"""

    @staticmethod
    def get_all():
        """Get all product images"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT image_id, product_id, image_url, is_main 
                FROM product_images
            """)
            rows = cursor.fetchall()
            return [ProductImage.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(image_id):
        """Get product image by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT image_id, product_id, image_url, is_main 
                FROM product_images WHERE image_id = %s
            """, (image_id,))
            row = cursor.fetchone()
            return ProductImage.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_product(product_id):
        """Get all images for a product"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT image_id, product_id, image_url, is_main 
                FROM product_images WHERE product_id = %s
            """, (product_id,))
            rows = cursor.fetchall()
            return [ProductImage.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_main_image(product_id):
        """Get main image for a product"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT image_id, product_id, image_url, is_main 
                FROM product_images WHERE product_id = %s AND is_main = 1
            """, (product_id,))
            row = cursor.fetchone()
            return ProductImage.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(image):
        """Create a new product image"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO product_images (product_id, image_url, is_main) 
                VALUES (%s, %s, %s)
            """, (image.product_id, image.image_url, image.is_main))
            connection.commit()
            image.image_id = cursor.lastrowid
            return image
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(image):
        """Update an existing product image"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE product_images 
                SET product_id = %s, image_url = %s, is_main = %s 
                WHERE image_id = %s
            """, (image.product_id, image.image_url, image.is_main, image.image_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(image_id):
        """Delete a product image by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM product_images WHERE image_id = %s", (image_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

