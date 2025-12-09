from flask import request, jsonify
from . import order_item_bp
from app.my_project.service import OrderItemService


@order_item_bp.route('', methods=['GET'])
def get_all_order_items():
    """Get all order items"""
    try:
        order_items = OrderItemService.get_all()
        return jsonify({'success': True, 'data': order_items}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_item_bp.route('/<int:order_item_id>', methods=['GET'])
def get_order_item(order_item_id):
    """Get order item by ID"""
    try:
        order_item = OrderItemService.get_by_id(order_item_id)
        if order_item is None:
            return jsonify({'success': False, 'error': 'Order item not found'}), 404
        return jsonify({'success': True, 'data': order_item}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_item_bp.route('/order/<int:order_id>', methods=['GET'])
def get_items_by_order(order_id):
    """Get all items for an order"""
    try:
        order_items = OrderItemService.get_by_order(order_id)
        return jsonify({'success': True, 'data': order_items}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_item_bp.route('', methods=['POST'])
def create_order_item():
    """Create a new order item"""
    try:
        data = request.get_json()
        order_item = OrderItemService.create(data)
        return jsonify({'success': True, 'data': order_item, 'message': 'Order item created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_item_bp.route('/<int:order_item_id>', methods=['PUT'])
def update_order_item(order_item_id):
    """Update an existing order item"""
    try:
        data = request.get_json()
        order_item = OrderItemService.update(order_item_id, data)
        if order_item is None:
            return jsonify({'success': False, 'error': 'Order item not found'}), 404
        return jsonify({'success': True, 'data': order_item, 'message': 'Order item updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@order_item_bp.route('/<int:order_item_id>', methods=['DELETE'])
def delete_order_item(order_item_id):
    """Delete an order item"""
    try:
        success = OrderItemService.delete(order_item_id)
        if not success:
            return jsonify({'success': False, 'error': 'Order item not found'}), 404
        return jsonify({'success': True, 'message': 'Order item deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

