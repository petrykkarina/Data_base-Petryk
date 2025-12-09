"""
Setup script for Rozetka Flask Application
Run this script to initialize the database
"""

import mysql.connector
import os


def setup_database():
    """Setup the database by running the SQL script"""
    print("=" * 50)
    print("Rozetka Database Setup")
    print("=" * 50)
    
    # Get MySQL credentials
    host = input("Enter MySQL host (default: localhost): ") or "localhost"
    user = input("Enter MySQL user (default: root): ") or "root"
    password = input("Enter MySQL password: ")
    port = input("Enter MySQL port (default: 3306): ") or "3306"
    
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=int(port)
        )
        cursor = connection.cursor()
        
        # Read SQL file
        sql_file_path = os.path.join(os.path.dirname(__file__), 'data.sql')
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()
        
        # Execute SQL statements
        for statement in sql_script.split(';'):
            statement = statement.strip()
            if statement:
                try:
                    cursor.execute(statement)
                except mysql.connector.Error as e:
                    print(f"Warning: {e}")
        
        connection.commit()
        print("\n✅ Database setup completed successfully!")
        print("Database 'rozetka_db' has been created with sample data.")
        
        # Update config file
        config_path = os.path.join(os.path.dirname(__file__), 'app', 'config', 'app.yml')
        with open(config_path, 'r') as file:
            config_content = file.read()
        
        config_content = config_content.replace('host: "localhost"', f'host: "{host}"')
        config_content = config_content.replace('user: "root"', f'user: "{user}"')
        config_content = config_content.replace('password: ""', f'password: "{password}"')
        config_content = config_content.replace('port: 3306', f'port: {port}')
        
        with open(config_path, 'w') as file:
            file.write(config_content)
        
        print("✅ Configuration file updated with your credentials.")
        print("\nYou can now run the application with: python app.py")
        
    except mysql.connector.Error as e:
        print(f"\n❌ Error: {e}")
        print("Please check your MySQL credentials and try again.")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    setup_database()

