import mysql.connector
from mysql.connector import pooling
import yaml
import os

class Config:
    SECRET_KEY = "supersecretkey"
    DEBUG = True
    TESTING = False

    # --- ВАШІ НАЛАШТУВАННЯ (ЗМІНЮЙТЕ ТУТ) ---
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "1009"  # <--- Ваш пароль тепер точно спрацює
    MYSQL_DB = "rozetka_db"
    MYSQL_PORT = 3306
    # ----------------------------------------

    _connection_pool = None

    @classmethod
    def load_from_yaml(cls, yaml_path=None):
        """
        Ми вимкнули завантаження з YAML, щоб пароль точно брався з коду вище.
        Якщо захочете повернути YAML, просто розкоментуйте рядки нижче.
        """
        pass
        # ---if yaml_path is None:
        #---    yaml_path = os.path.join(os.path.dirname(__file__), 'app.yml')
        
        #--- try:
        #  ---   with open(yaml_path, 'r') as file:
        #   ---      config = yaml.safe_load(file)
        #    ---     db_config = config.get('database', {})
        #     ---    cls.MYSQL_HOST = db_config.get('host', cls.MYSQL_HOST)
        #       ---  cls.MYSQL_USER = db_config.get('user', cls.MYSQL_USER)
        #       ---  cls.MYSQL_PASSWORD = db_config.get('password', cls.MYSQL_PASSWORD)
        #       ---  cls.MYSQL_DB = db_config.get('name', cls.MYSQL_DB)
        #       ---  cls.MYSQL_PORT = db_config.get('port', cls.MYSQL_PORT)
        #--- except FileNotFoundError:
        #   ---  print("Config file not found, using defaults")

    @classmethod
    def load_from_input(cls):
        """Load configuration from user input"""
        cls.MYSQL_HOST = input("Enter MySQL host (default: localhost): ") or "localhost"
        cls.MYSQL_USER = input("Enter MySQL user (default: root): ") or "root"
        cls.MYSQL_PASSWORD = input("Enter MySQL password: ") or "1009"
        cls.MYSQL_DB = input("Enter MySQL database name: ")
        port_input = input("Enter MySQL port (default: 3306): ")
        cls.MYSQL_PORT = int(port_input) if port_input else 3306

    @classmethod
    def init_connection_pool(cls):
        """Initialize connection pool"""
        # Перевіряємо, чи існує пул, щоб не створювати зайві
        if cls._connection_pool is None:
            cls._connection_pool = pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=5,
                host=cls.MYSQL_HOST,
                user=cls.MYSQL_USER,
                password=cls.MYSQL_PASSWORD,
                database=cls.MYSQL_DB,
                port=cls.MYSQL_PORT
            )

    @classmethod
    def get_connection(cls):
        """Get a connection from the pool"""
        if cls._connection_pool is None:
            cls.init_connection_pool()
        return cls._connection_pool.get_connection()

    @classmethod
    def get_db_connection(cls):
        """Get a direct database connection"""
        return mysql.connector.connect(
            host=cls.MYSQL_HOST,
            user=cls.MYSQL_USER,
            password=cls.MYSQL_PASSWORD,
            database=cls.MYSQL_DB,
            port=cls.MYSQL_PORT
        )