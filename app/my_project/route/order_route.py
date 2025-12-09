from flask import request, jsonify
from . import order_bp
from app.my_project.service import OrderService


@order_bp.route('', methods=['GET'])
def get_all_orders():
    """Get all orders"""
    try:
        orders = OrderService.get_all()
        return jsonify({'success': True, 'data': orders}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get order by ID"""
    try:
        order = OrderService.get_by_id(order_id)
        if order is None:
            return jsonify({'success': False, 'error': 'Order not found'}), 404
        return jsonify({'success': True, 'data': order}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_bp.route('/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    """Get all orders for a user"""
    try:
        orders = OrderService.get_by_user(user_id)
        return jsonify({'success': True, 'data': orders}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_bp.route('/status/<status>', methods=['GET'])
def get_orders_by_status(status):
    """Get all orders with a specific status"""
    try:
        orders = OrderService.get_by_status(status)
        return jsonify({'success': True, 'data': orders}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_bp.route('', methods=['POST'])
def create_order():
    """Create a new order"""
    try:
        data = request.get_json()
        order = OrderService.create(data)
        return jsonify({'success': True, 'data': order, 'message': 'Order created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an existing order"""
    try:
        data = request.get_json()
        order = OrderService.update(order_id, data)
        if order is None:
            return jsonify({'success': False, 'error': 'Order not found'}), 404
        return jsonify({'success': True, 'data': order, 'message': 'Order updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an order"""
    try:
        success = OrderService.delete(order_id)
        if not success:
            return jsonify({'success': False, 'error': 'Order not found'}), 404
        return jsonify({'success': True, 'message': 'Order deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

