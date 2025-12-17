from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='1009',
        database='rozetka_db'
    )

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.callproc('sp_add_product', (name, price, description))
        connection.commit()
        return jsonify({'message': 'Product added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/orders/add-item', methods=['POST'])
def add_order_item():
    data = request.json
    order_id = data.get('order_id')
    product_name = data.get('product_name')
    quantity = data.get('quantity')
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.callproc('sp_add_product_to_order_by_name', (order_id, product_name, quantity))
        connection.commit()
        return jsonify({'message': 'Product added to order successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/users/insert-nonames', methods=['POST'])
def insert_nonames():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.callproc('sp_insert_nonames')
        connection.commit()
        return jsonify({'message': 'Inserted 10 Noname users successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/products/avg-price', methods=['GET'])
def get_avg_price():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT fn_get_avg_product_price()")
            result = cursor.fetchone()
        return jsonify({'mode': 'AVG', 'result': float(result[0])}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/products/split', methods=['POST'])
def split_products():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.callproc('sp_dynamic_split_products')
        connection.commit()
        return jsonify({'message': 'Products split into dynamic tables successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

@app.route('/products/add-note', methods=['POST'])
def add_product_note():
    data = request.json
    product_id = data.get('product_id')
    note_text = data.get('note_text')
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO product_notes (product_id, note_text) VALUES (%s, %s)", (product_id, note_text))
        connection.commit()
        return jsonify({'message': 'Note added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)