from app.config import Config
from app.my_project.domain import Subcategory


class SubcategoryDAO:
    """Data Access Object for Subcategory entity"""

    @staticmethod
    def get_all():
        """Get all subcategories"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT subcategory_id, category_id, subcategory_name, description 
                FROM subcategories
            """)
            rows = cursor.fetchall()
            return [Subcategory.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(subcategory_id):
        """Get subcategory by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT subcategory_id, category_id, subcategory_name, description 
                FROM subcategories WHERE subcategory_id = %s
            """, (subcategory_id,))
            row = cursor.fetchone()
            return Subcategory.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_category(category_id):
        """Get all subcategories for a category"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT subcategory_id, category_id, subcategory_name, description 
                FROM subcategories WHERE category_id = %s
            """, (category_id,))
            rows = cursor.fetchall()
            return [Subcategory.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(subcategory):
        """Create a new subcategory"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO subcategories (category_id, subcategory_name, description) 
                VALUES (%s, %s, %s)
            """, (subcategory.category_id, subcategory.subcategory_name, subcategory.description))
            connection.commit()
            subcategory.subcategory_id = cursor.lastrowid
            return subcategory
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(subcategory):
        """Update an existing subcategory"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE subcategories 
                SET category_id = %s, subcategory_name = %s, description = %s 
                WHERE subcategory_id = %s
            """, (subcategory.category_id, subcategory.subcategory_name, 
                  subcategory.description, subcategory.subcategory_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(subcategory_id):
        """Delete a subcategory by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM subcategories WHERE subcategory_id = %s", (subcategory_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

