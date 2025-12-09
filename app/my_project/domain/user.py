class User:
    """Domain model for User entity"""
    
    def __init__(self, user_id=None, role_id=None, full_name=None, email=None,
                 password_hash=None, phone=None, created_at=None):
        self.user_id = user_id
        self.role_id = role_id
        self.full_name = full_name
        self.email = email
        self.password_hash = password_hash
        self.phone = phone
        self.created_at = created_at

    def to_dict(self):
        """Convert User to dictionary (DTO)"""
        return {
            'user_id': self.user_id,
            'role_id': self.role_id,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'created_at': str(self.created_at) if self.created_at else None
        }

    def to_dict_with_password(self):
        """Convert User to dictionary including password hash"""
        data = self.to_dict()
        data['password_hash'] = self.password_hash
        return data

    @staticmethod
    def from_dict(data):
        """Create User from dictionary"""
        return User(
            user_id=data.get('user_id'),
            role_id=data.get('role_id'),
            full_name=data.get('full_name'),
            email=data.get('email'),
            password_hash=data.get('password_hash'),
            phone=data.get('phone'),
            created_at=data.get('created_at')
        )

    @staticmethod
    def from_db_row(row):
        """Create User from database row tuple"""
        if row is None:
            return None
        return User(
            user_id=row[0],
            role_id=row[1],
            full_name=row[2],
            email=row[3],
            password_hash=row[4],
            phone=row[5],
            created_at=row[6]
        )

    def __repr__(self):
        return f"User(user_id={self.user_id}, email='{self.email}')"

