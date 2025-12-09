from flask import request, jsonify
from . import payment_bp
from app.my_project.service import PaymentService


@payment_bp.route('', methods=['GET'])
def get_all_payments():
    """Get all payments"""
    try:
        payments = PaymentService.get_all()
        return jsonify({'success': True, 'data': payments}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@payment_bp.route('/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    """Get payment by ID"""
    try:
        payment = PaymentService.get_by_id(payment_id)
        if payment is None:
            return jsonify({'success': False, 'error': 'Payment not found'}), 404
        return jsonify({'success': True, 'data': payment}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@payment_bp.route('/order/<int:order_id>', methods=['GET'])
def get_payment_by_order(order_id):
    """Get payment for an order"""
    try:
        payment = PaymentService.get_by_order(order_id)
        if payment is None:
            return jsonify({'success': False, 'error': 'Payment not found'}), 404
        return jsonify({'success': True, 'data': payment}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@payment_bp.route('', methods=['POST'])
def create_payment():
    """Create a new payment"""
    try:
        data = request.get_json()
        payment = PaymentService.create(data)
        return jsonify({'success': True, 'data': payment, 'message': 'Payment created successfully'}), 201
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@payment_bp.route('/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    """Update an existing payment"""
    try:
        data = request.get_json()
        payment = PaymentService.update(payment_id, data)
        if payment is None:
            return jsonify({'success': False, 'error': 'Payment not found'}), 404
        return jsonify({'success': True, 'data': payment, 'message': 'Payment updated successfully'}), 200
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@payment_bp.route('/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    """Delete a payment"""
    try:
        success = PaymentService.delete(payment_id)
        if not success:
            return jsonify({'success': False, 'error': 'Payment not found'}), 404
        return jsonify({'success': True, 'message': 'Payment deleted successfully'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

