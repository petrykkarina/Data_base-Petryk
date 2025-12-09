from flask import request, jsonify
from . import role_bp
from app.my_project.service import RoleService


@role_bp.route('', methods=['GET'])
def get_all_roles():
    """Get all roles"""
    try:
        roles = RoleService.get_all()
        return jsonify({'success': True, 'data': roles}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@role_bp.route('/<int:role_id>', methods=['GET'])
def get_role(role_id):
    """Get role by ID"""
    try:
        role = RoleService.get_by_id(role_id)
        if role is None:
            return jsonify({'success': False, 'error': 'Role not found'}), 404
        return jsonify({'success': True, 'data': role}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@role_bp.route('', methods=['POST'])
def create_role():
    """Create a new role"""
    try:
        data = request.get_json()
        role = RoleService.create(data)
        return jsonify({'success': True, 'data': role, 'message': 'Role created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@role_bp.route('/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    """Update an existing role"""
    try:
        data = request.get_json()
        role = RoleService.update(role_id, data)
        if role is None:
            return jsonify({'success': False, 'error': 'Role not found'}), 404
        return jsonify({'success': True, 'data': role, 'message': 'Role updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@role_bp.route('/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    """Delete a role"""
    try:
        success = RoleService.delete(role_id)
        if not success:
            return jsonify({'success': False, 'error': 'Role not found'}), 404
        return jsonify({'success': True, 'message': 'Role deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

