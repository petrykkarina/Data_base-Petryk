from flask import request, jsonify
from . import subcategory_bp
from app.my_project.service import SubcategoryService


@subcategory_bp.route('', methods=['GET'])
def get_all_subcategories():
    """Get all subcategories"""
    try:
        subcategories = SubcategoryService.get_all()
        return jsonify({'success': True, 'data': subcategories}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@subcategory_bp.route('/<int:subcategory_id>', methods=['GET'])
def get_subcategory(subcategory_id):
    """Get subcategory by ID"""
    try:
        subcategory = SubcategoryService.get_by_id(subcategory_id)
        if subcategory is None:
            return jsonify({'success': False, 'error': 'Subcategory not found'}), 404
        return jsonify({'success': True, 'data': subcategory}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@subcategory_bp.route('/category/<int:category_id>', methods=['GET'])
def get_subcategories_by_category(category_id):
    """Get all subcategories for a category"""
    try:
        subcategories = SubcategoryService.get_by_category(category_id)
        return jsonify({'success': True, 'data': subcategories}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@subcategory_bp.route('', methods=['POST'])
def create_subcategory():
    """Create a new subcategory"""
    try:
        data = request.get_json()
        subcategory = SubcategoryService.create(data)
        return jsonify({'success': True, 'data': subcategory, 'message': 'Subcategory created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@subcategory_bp.route('/<int:subcategory_id>', methods=['PUT'])
def update_subcategory(subcategory_id):
    """Update an existing subcategory"""
    try:
        data = request.get_json()
        subcategory = SubcategoryService.update(subcategory_id, data)
        if subcategory is None:
            return jsonify({'success': False, 'error': 'Subcategory not found'}), 404
        return jsonify({'success': True, 'data': subcategory, 'message': 'Subcategory updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@subcategory_bp.route('/<int:subcategory_id>', methods=['DELETE'])
def delete_subcategory(subcategory_id):
    """Delete a subcategory"""
    try:
        success = SubcategoryService.delete(subcategory_id)
        if not success:
            return jsonify({'success': False, 'error': 'Subcategory not found'}), 404
        return jsonify({'success': True, 'message': 'Subcategory deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

