from app.config import Config
from app.my_project.domain import Category


class CategoryDAO:
    """Data Access Object for Category entity"""

    @staticmethod
    def get_all():
        """Get all categories"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT category_id, category_name, description FROM categories")
            rows = cursor.fetchall()
            return [Category.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(category_id):
        """Get category by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT category_id, category_name, description FROM categories WHERE category_id = %s",
                (category_id,)
            )
            row = cursor.fetchone()
            return Category.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(category):
        """Create a new category"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO categories (category_name, description) VALUES (%s, %s)",
                (category.category_name, category.description)
            )
            connection.commit()
            category.category_id = cursor.lastrowid
            return category
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(category):
        """Update an existing category"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE categories SET category_name = %s, description = %s WHERE category_id = %s",
                (category.category_name, category.description, category.category_id)
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(category_id):
        """Delete a category by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM categories WHERE category_id = %s", (category_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

