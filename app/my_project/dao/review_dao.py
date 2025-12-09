from app.config import Config
from app.my_project.domain import Review


class ReviewDAO:
    """Data Access Object for Review entity"""

    @staticmethod
    def get_all():
        """Get all reviews"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT review_id, user_id, product_id, rating, comment, created_at 
                FROM reviews
            """)
            rows = cursor.fetchall()
            return [Review.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_id(review_id):
        """Get review by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT review_id, user_id, product_id, rating, comment, created_at 
                FROM reviews WHERE review_id = %s
            """, (review_id,))
            row = cursor.fetchone()
            return Review.from_db_row(row)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_product(product_id):
        """Get all reviews for a product"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT review_id, user_id, product_id, rating, comment, created_at 
                FROM reviews WHERE product_id = %s
            """, (product_id,))
            rows = cursor.fetchall()
            return [Review.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_by_user(user_id):
        """Get all reviews by a user"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT review_id, user_id, product_id, rating, comment, created_at 
                FROM reviews WHERE user_id = %s
            """, (user_id,))
            rows = cursor.fetchall()
            return [Review.from_db_row(row) for row in rows]
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create(review):
        """Create a new review"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO reviews (user_id, product_id, rating, comment, created_at)
                VALUES (%s, %s, %s, %s, NOW())
            """, (review.user_id, review.product_id, review.rating, review.comment))
            connection.commit()
            review.review_id = cursor.lastrowid
            return review
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update(review):
        """Update an existing review"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE reviews 
                SET rating = %s, comment = %s 
                WHERE review_id = %s
            """, (review.rating, review.comment, review.review_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete(review_id):
        """Delete a review by ID"""
        connection = Config.get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM reviews WHERE review_id = %s", (review_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            connection.close()

