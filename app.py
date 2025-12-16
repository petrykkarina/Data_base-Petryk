"""
Rozetka Flask Backend Application
Main entry point for the application
"""

from app import create_app
from flask import Flask, jsonify, request
from app.config.config import Config

app = create_app()

@app.route('/api/roles/<int:id>/details', methods=['GET'])
def get_role_with_users(id):
    connection = None
    try:
        connection = Config.get_connection()
        cursor = connection.cursor(dictionary=True)

        # 1. Отримуємо роль
        cursor.execute("SELECT * FROM roles WHERE role_id = %s", (id,))
        role = cursor.fetchone()

        if not role:
            return jsonify({"error": "Role not found"}), 404

        # 2. Отримуємо користувачів (ТУТ БУЛА ПОМИЛКА)
        # Використовуємо SELECT *, щоб не вгадувати назви (username/user_name тощо)
        cursor.execute("SELECT * FROM users WHERE role_id = %s", (id,))
        users = cursor.fetchall()

        response_data = {
            "role_info": role,
            "users_list": users,
            "total_users": len(users)
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection:
            if 'cursor' in locals() and cursor:
                cursor.close()
            connection.close()

@app.route('/api/orders/<int:order_id>/products', methods=['GET'])
def get_order_products_mm(order_id):
    connection = None
    try:
        connection = Config.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM orders WHERE order_id = %s", (order_id,))
        order = cursor.fetchone()

        if not order:
            return jsonify({"error": "Order not found"}), 404

        sql = """
        SELECT p.* FROM products p
        JOIN order_items oi ON p.product_id = oi.product_id
        WHERE oi.order_id = %s
        """
        cursor.execute(sql, (order_id,))
        products = cursor.fetchall()

        response_data = {
            "order_info": order,
            "products_list": products,
            "total_products": len(products)
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection:
            if 'cursor' in locals() and cursor:
                cursor.close()
            connection.close()

if __name__ == '__main__':
    print("=" * 50)
    print("Rozetka API Server")
    print("=" * 50)
    print("Available endpoints:")
    print("  GET    /api/roles              - Get all roles")
    print("  GET    /api/users              - Get all users")
    print("  GET    /api/categories         - Get all categories")
    print("  GET    /api/subcategories      - Get all subcategories")
    print("  GET    /api/products           - Get all products")
    print("  GET    /api/product-attributes - Get all product attributes")
    print("  GET    /api/product-images     - Get all product images")
    print("  GET    /api/reviews            - Get all reviews")
    print("  GET    /api/orders             - Get all orders")
    print("  GET    /api/order-items        - Get all order items")
    print("  GET    /api/payments           - Get all payments")
    print("=" * 50)
    print("Each endpoint supports: GET, POST, PUT, DELETE")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=True)

