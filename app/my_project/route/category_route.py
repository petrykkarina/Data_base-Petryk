from flask import request, jsonify
from . import category_bp
from app.my_project.service import CategoryService


@category_bp.route('', methods=['GET'])
def get_all_categories():
    """Get all categories"""
    try:
        categories = CategoryService.get_all()
        return jsonify({'success': True, 'data': categories}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@category_bp.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """Get category by ID"""
    try:
        category = CategoryService.get_by_id(category_id)
        if category is None:
            return jsonify({'success': False, 'error': 'Category not found'}), 404
        return jsonify({'success': True, 'data': category}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@category_bp.route('', methods=['POST'])
def create_category():
    """Create a new category"""
    try:
        data = request.get_json()
        category = CategoryService.create(data)
        return jsonify({'success': True, 'data': category, 'message': 'Category created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@category_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """Update an existing category"""
    try:
        data = request.get_json()
        category = CategoryService.update(category_id, data)
        if category is None:
            return jsonify({'success': False, 'error': 'Category not found'}), 404
        return jsonify({'success': True, 'data': category, 'message': 'Category updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@category_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Delete a category"""
    try:
        success = CategoryService.delete(category_id)
        if not success:
            return jsonify({'success': False, 'error': 'Category not found'}), 404
        return jsonify({'success': True, 'message': 'Category deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

