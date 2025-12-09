from flask import request, jsonify
from . import user_bp
from app.my_project.service import UserService


@user_bp.route('', methods=['GET'])
def get_all_users():
    """Get all users"""
    try:
        users = UserService.get_all()
        return jsonify({'success': True, 'data': users}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    try:
        user = UserService.get_by_id(user_id)
        if user is None:
            return jsonify({'success': False, 'error': 'User not found'}), 404
        return jsonify({'success': True, 'data': user}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@user_bp.route('/email/<email>', methods=['GET'])
def get_user_by_email(email):
    """Get user by email"""
    try:
        user = UserService.get_by_email(email)
        if user is None:
            return jsonify({'success': False, 'error': 'User not found'}), 404
        return jsonify({'success': True, 'data': user}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@user_bp.route('', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        user = UserService.create(data)
        return jsonify({'success': True, 'data': user, 'message': 'User created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user"""
    try:
        data = request.get_json()
        user = UserService.update(user_id, data)
        if user is None:
            return jsonify({'success': False, 'error': 'User not found'}), 404
        return jsonify({'success': True, 'data': user, 'message': 'User updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    try:
        success = UserService.delete(user_id)
        if not success:
            return jsonify({'success': False, 'error': 'User not found'}), 404
        return jsonify({'success': True, 'message': 'User deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

