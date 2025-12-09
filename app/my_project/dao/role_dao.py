from app.config import Config
from app.my_project.domain import Role


class RoleDAO:
    """Data Access Object for Role entity"""

    @staticmethod
    def get_all():
        """Get all roles"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT role_id, role_name FROM roles")
            rows = cursor.fetchall()
            return [Role.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(role_id):
        """Get role by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT role_id, role_name FROM roles WHERE role_id = %s",
                (role_id,)
            )
            row = cursor.fetchone()
            return Role.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(role):
        """Create a new role"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO roles (role_name) VALUES (%s)",
                (role.role_name,)
            )
            connection.commit()
            role.role_id = cursor.lastrowid
            return role
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(role):
        """Update an existing role"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE roles SET role_name = %s WHERE role_id = %s",
                (role.role_name, role.role_id)
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(role_id):
        """Delete a role by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM roles WHERE role_id = %s",
                (role_id,)
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

