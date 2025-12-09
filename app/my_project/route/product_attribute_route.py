from flask import request, jsonify
from . import product_attribute_bp
from app.my_project.service import ProductAttributeService


@product_attribute_bp.route('', methods=['GET'])
def get_all_product_attributes():
    """Get all product attributes"""
    try:
        attributes = ProductAttributeService.get_all()
        return jsonify({'success': True, 'data': attributes}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_attribute_bp.route('/<int:attribute_id>', methods=['GET'])
def get_product_attribute(attribute_id):
    """Get product attribute by ID"""
    try:
        attribute = ProductAttributeService.get_by_id(attribute_id)
        if attribute is None:
            return jsonify({'success': False, 'error': 'Product attribute not found'}), 404
        return jsonify({'success': True, 'data': attribute}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_attribute_bp.route('/product/<int:product_id>', methods=['GET'])
def get_attributes_by_product(product_id):
    """Get all attributes for a product"""
    try:
        attributes = ProductAttributeService.get_by_product(product_id)
        return jsonify({'success': True, 'data': attributes}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_attribute_bp.route('', methods=['POST'])
def create_product_attribute():
    """Create a new product attribute"""
    try:
        data = request.get_json()
        attribute = ProductAttributeService.create(data)
        return jsonify({'success': True, 'data': attribute, 'message': 'Product attribute created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_attribute_bp.route('/<int:attribute_id>', methods=['PUT'])
def update_product_attribute(attribute_id):
    """Update an existing product attribute"""
    try:
        data = request.get_json()
        attribute = ProductAttributeService.update(attribute_id, data)
        if attribute is None:
            return jsonify({'success': False, 'error': 'Product attribute not found'}), 404
        return jsonify({'success': True, 'data': attribute, 'message': 'Product attribute updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@product_attribute_bp.route('/<int:attribute_id>', methods=['DELETE'])
def delete_product_attribute(attribute_id):
    """Delete a product attribute"""
    try:
        success = ProductAttributeService.delete(attribute_id)
        if not success:
            return jsonify({'success': False, 'error': 'Product attribute not found'}), 404
        return jsonify({'success': True, 'message': 'Product attribute deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

