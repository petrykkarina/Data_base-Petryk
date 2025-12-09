class Review:
    """Domain model for Review entity"""
    
    def __init__(self, review_id=None, user_id=None, product_id=None,
                 rating=None, comment=None, created_at=None):
        self.review_id = review_id
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating
        self.comment = comment
        self.created_at = created_at

    def to_dict(self):
        """Convert Review to dictionary (DTO)"""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': str(self.created_at) if self.created_at else None
        }

    @staticmethod
    def from_dict(data):
        """Create Review from dictionary"""
        return Review(
            review_id=data.get('review_id'),
            user_id=data.get('user_id'),
            product_id=data.get('product_id'),
            rating=data.get('rating'),
            comment=data.get('comment'),
            created_at=data.get('created_at')
        )

    @staticmethod
    def from_db_row(row):
        """Create Review from database row tuple"""
        if row is None:
            return None
        return Review(
            review_id=row[0],
            user_id=row[1],
            product_id=row[2],
            rating=row[3],
            comment=row[4],
            created_at=row[5]
        )

    def __repr__(self):
        return f"Review(review_id={self.review_id}, rating={self.rating})"

