from werkzeug.security import generate_password_hash
from app.my_project.dao import UserDAO
from app.my_project.domain import User


class UserService:
    """Service layer for User entity with business logic"""

    @staticmethod
    def get_all():
        """Get all users"""
        users = UserDAO.get_all()
        return [user.to_dict() for user in users]

    @staticmethod
    def get_by_id(user_id):
        """Get user by ID"""
        user = UserDAO.get_by_id(user_id)
        if user is None:
            return None
        return user.to_dict()

    @staticmethod
    def get_by_email(email):
        """Get user by email"""
        user = UserDAO.get_by_email(email)
        if user is None:
            return None
        return user.to_dict()

    @staticmethod
    def create(data):
        """Create a new user"""
        if not data.get('email'):
            raise ValueError("Email is required")
        if not data.get('password'):
            raise ValueError("Password is required")
        if not data.get('full_name'):
            raise ValueError("Full name is required")
        
        # Check if email already exists
        existing_user = UserDAO.get_by_email(data['email'])
        if existing_user:
            raise ValueError("Email already exists")
        
        # Hash password
        password_hash = generate_password_hash(data['password'])
        
        user = User(
            role_id=data.get('role_id', 2),  # Default to regular user role
            full_name=data['full_name'],
            email=data['email'],
            password_hash=password_hash,
            phone=data.get('phone')
        )
        
        created_user = UserDAO.create(user)
        return created_user.to_dict()

    @staticmethod
    def update(user_id, data):
        """Update an existing user"""
        existing_user = UserDAO.get_by_id(user_id)
        if existing_user is None:
            return None
        
        existing_user.full_name = data.get('full_name', existing_user.full_name)
        existing_user.email = data.get('email', existing_user.email)
        existing_user.phone = data.get('phone', existing_user.phone)
        existing_user.role_id = data.get('role_id', existing_user.role_id)
        
        success = UserDAO.update(existing_user)
        if success:
            return existing_user.to_dict()
        return None

    @staticmethod
    def delete(user_id):
        """Delete a user by ID"""
        existing_user = UserDAO.get_by_id(user_id)
        if existing_user is None:
            return False
        
        return UserDAO.delete(user_id)

