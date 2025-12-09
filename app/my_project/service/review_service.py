from app.my_project.dao import ReviewDAO
from app.my_project.domain import Review


class ReviewService:
    """Service layer for Review entity with business logic"""

    @staticmethod
    def get_all():
        """Get all reviews"""
        reviews = ReviewDAO.get_all()
        return [review.to_dict() for review in reviews]

    @staticmethod
    def get_by_id(review_id):
        """Get review by ID"""
        review = ReviewDAO.get_by_id(review_id)
        if review is None:
            return None
        return review.to_dict()

    @staticmethod
    def get_by_product(product_id):
        """Get all reviews for a product"""
        reviews = ReviewDAO.get_by_product(product_id)
        return [review.to_dict() for review in reviews]

    @staticmethod
    def get_by_user(user_id):
        """Get all reviews by a user"""
        reviews = ReviewDAO.get_by_user(user_id)
        return [review.to_dict() for review in reviews]

    @staticmethod
    def create(data):
        """Create a new review"""
        if not data.get('user_id'):
            raise ValueError("User ID is required")
        if not data.get('product_id'):
            raise ValueError("Product ID is required")
        if not data.get('rating'):
            raise ValueError("Rating is required")
        
        # Validate rating
        rating = data.get('rating')
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        
        review = Review.from_dict(data)
        created_review = ReviewDAO.create(review)
        return created_review.to_dict()

    @staticmethod
    def update(review_id, data):
        """Update an existing review"""
        existing_review = ReviewDAO.get_by_id(review_id)
        if existing_review is None:
            return None
        
        if data.get('rating'):
            rating = data.get('rating')
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5")
            existing_review.rating = rating
        
        existing_review.comment = data.get('comment', existing_review.comment)
        
        success = ReviewDAO.update(existing_review)
        if success:
            return existing_review.to_dict()
        return None

    @staticmethod
    def delete(review_id):
        """Delete a review by ID"""
        existing_review = ReviewDAO.get_by_id(review_id)
        if existing_review is None:
            return False
        
        return ReviewDAO.delete(review_id)

