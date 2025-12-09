from flask import request, jsonify
from . import review_bp
from app.my_project.service import ReviewService


@review_bp.route('', methods=['GET'])
def get_all_reviews():
    """Get all reviews"""
    try:
        reviews = ReviewService.get_all()
        return jsonify({'success': True, 'data': reviews}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    """Get review by ID"""
    try:
        review = ReviewService.get_by_id(review_id)
        if review is None:
            return jsonify({'success': False, 'error': 'Review not found'}), 404
        return jsonify({'success': True, 'data': review}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@review_bp.route('/product/<int:product_id>', methods=['GET'])
def get_reviews_by_product(product_id):
    """Get all reviews for a product"""
    try:
        reviews = ReviewService.get_by_product(product_id)
        return jsonify({'success': True, 'data': reviews}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@review_bp.route('/user/<int:user_id>', methods=['GET'])
def get_reviews_by_user(user_id):
    """Get all reviews by a user"""
    try:
        reviews = ReviewService.get_by_user(user_id)
        return jsonify({'success': True, 'data': reviews}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@review_bp.route('', methods=['POST'])
def create_review():
    """Create a new review"""
    try:
        data = request.get_json()
        review = ReviewService.create(data)
        return jsonify({'success': True, 'data': review, 'message': 'Review created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    """Update an existing review"""
    try:
        data = request.get_json()
        review = ReviewService.update(review_id, data)
        if review is None:
            return jsonify({'success': False, 'error': 'Review not found'}), 404
        return jsonify({'success': True, 'data': review, 'message': 'Review updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """Delete a review"""
    try:
        success = ReviewService.delete(review_id)
        if not success:
            return jsonify({'success': False, 'error': 'Review not found'}), 404
        return jsonify({'success': True, 'message': 'Review deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

