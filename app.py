"""
Rozetka Flask Backend Application
Main entry point for the application
"""

from app import create_app

app = create_app()

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

