from app.config import Config
from app.my_project.domain import User


class UserDAO:
    """Data Access Object for User entity"""

    @staticmethod
    def get_all():
        """Get all users"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT user_id, role_id, full_name, email, password_hash, phone, created_at 
                FROM users
            """)
            rows = cursor.fetchall()
            return [User.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(user_id):
        """Get user by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT user_id, role_id, full_name, email, password_hash, phone, created_at 
                FROM users WHERE user_id = %s
            """, (user_id,))
            row = cursor.fetchone()
            return User.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_email(email):
        """Get user by email"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT user_id, role_id, full_name, email, password_hash, phone, created_at 
                FROM users WHERE email = %s
            """, (email,))
            row = cursor.fetchone()
            return User.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(user):
        """Create a new user"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO users (role_id, full_name, email, password_hash, phone, created_at)
                VALUES (%s, %s, %s, %s, %s, NOW())
            """, (user.role_id, user.full_name, user.email, user.password_hash, user.phone))
            connection.commit()
            user.user_id = cursor.lastrowid
            return user
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(user):
        """Update an existing user"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE users 
                SET role_id = %s, full_name = %s, email = %s, phone = %s
                WHERE user_id = %s
            """, (user.role_id, user.full_name, user.email, user.phone, user.user_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(user_id):
        """Delete a user by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

