from flask import request, jsonify
from . import product_bp
from app.my_project.service import ProductService


@product_bp.route('', methods=['GET'])
def get_all_products():
    """Get all products"""
    try:
        products = ProductService.get_all()
        return jsonify({'success': True, 'data': products}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get product by ID"""
    try:
        product = ProductService.get_by_id(product_id)
        if product is None:
            return jsonify({'success': False, 'error': 'Product not found'}), 404
        return jsonify({'success': True, 'data': product}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_bp.route('/subcategory/<int:subcategory_id>', methods=['GET'])
def get_products_by_subcategory(subcategory_id):
    """Get all products in a subcategory"""
    try:
        products = ProductService.get_by_subcategory(subcategory_id)
        return jsonify({'success': True, 'data': products}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_bp.route('', methods=['POST'])
def create_product():
    """Create a new product"""
    try:
        data = request.get_json()
        product = ProductService.create(data)
        return jsonify({'success': True, 'data': product, 'message': 'Product created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product"""
    try:
        data = request.get_json()
        product = ProductService.update(product_id, data)
        if product is None:
            return jsonify({'success': False, 'error': 'Product not found'}), 404
        return jsonify({'success': True, 'data': product, 'message': 'Product updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    try:
        success = ProductService.delete(product_id)
        if not success:
            return jsonify({'success': False, 'error': 'Product not found'}), 404
        return jsonify({'success': True, 'message': 'Product deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

