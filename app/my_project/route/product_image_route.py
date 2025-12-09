from flask import request, jsonify
from . import product_image_bp
from app.my_project.service import ProductImageService


@product_image_bp.route('', methods=['GET'])
def get_all_product_images():
    """Get all product images"""
    try:
        images = ProductImageService.get_all()
        return jsonify({'success': True, 'data': images}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_image_bp.route('/<int:image_id>', methods=['GET'])
def get_product_image(image_id):
    """Get product image by ID"""
    try:
        image = ProductImageService.get_by_id(image_id)
        if image is None:
            return jsonify({'success': False, 'error': 'Product image not found'}), 404
        return jsonify({'success': True, 'data': image}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_image_bp.route('/product/<int:product_id>', methods=['GET'])
def get_images_by_product(product_id):
    """Get all images for a product"""
    try:
        images = ProductImageService.get_by_product(product_id)
        return jsonify({'success': True, 'data': images}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_image_bp.route('/product/<int:product_id>/main', methods=['GET'])
def get_main_image(product_id):
    """Get main image for a product"""
    try:
        image = ProductImageService.get_main_image(product_id)
        if image is None:
            return jsonify({'success': False, 'error': 'Main image not found'}), 404
        return jsonify({'success': True, 'data': image}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_image_bp.route('', methods=['POST'])
def create_product_image():
    """Create a new product image"""
    try:
        data = request.get_json()
        image = ProductImageService.create(data)
        return jsonify({'success': True, 'data': image, 'message': 'Product image created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_image_bp.route('/<int:image_id>', methods=['PUT'])
def update_product_image(image_id):
    """Update an existing product image"""
    try:
        data = request.get_json()
        image = ProductImageService.update(image_id, data)
        if image is None:
            return jsonify({'success': False, 'error': 'Product image not found'}), 404
        return jsonify({'success': True, 'data': image, 'message': 'Product image updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_image_bp.route('/<int:image_id>', methods=['DELETE'])
def delete_product_image(image_id):
    """Delete a product image"""
    try:
        success = ProductImageService.delete(image_id)
        if not success:
            return jsonify({'success': False, 'error': 'Product image not found'}), 404
        return jsonify({'success': True, 'message': 'Product image deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

