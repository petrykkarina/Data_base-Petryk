from app.my_project.dao import RoleDAO
from app.my_project.domain import Role


class RoleService:
    """Service layer for Role entity with business logic"""

    @staticmethod
    def get_all():
        """Get all roles"""
        roles = RoleDAO.get_all()
        return [role.to_dict() for role in roles]

    @staticmethod
    def get_by_id(role_id):
        """Get role by ID"""
        role = RoleDAO.get_by_id(role_id)
        if role is None:
            return None
        return role.to_dict()

    @staticmethod
    def create(data):
        """Create a new role"""
        if not data.get('role_name'):
            raise ValueError("Role name is required")
        
        role = Role.from_dict(data)
        created_role = RoleDAO.create(role)
        return created_role.to_dict()

    @staticmethod
    def update(role_id, data):
        """Update an existing role"""
        existing_role = RoleDAO.get_by_id(role_id)
        if existing_role is None:
            return None
        
        existing_role.role_name = data.get('role_name', existing_role.role_name)
        
        success = RoleDAO.update(existing_role)
        if success:
            return existing_role.to_dict()
        return None

    @staticmethod
    def delete(role_id):
        """Delete a role by ID"""
        existing_role = RoleDAO.get_by_id(role_id)
        if existing_role is None:
            return False
        
        return RoleDAO.delete(role_id)

