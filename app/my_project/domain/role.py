class Role:
    """Domain model for Role entity"""
    
    def __init__(self, role_id=None, role_name=None):
        self.role_id = role_id
        self.role_name = role_name

    def to_dict(self):
        """Convert Role to dictionary (DTO)"""
        return {
            'role_id': self.role_id,
            'role_name': self.role_name
        }

    @staticmethod
    def from_dict(data):
        """Create Role from dictionary"""
        return Role(
            role_id=data.get('role_id'),
            role_name=data.get('role_name')
        )

    @staticmethod
    def from_db_row(row):
        """Create Role from database row tuple"""
        if row is None:
            return None
        return Role(
            role_id=row[0],
            role_name=row[1]
        )

    def __repr__(self):
        return f"Role(role_id={self.role_id}, role_name='{self.role_name}')"

