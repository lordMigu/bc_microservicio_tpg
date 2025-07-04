import os
import pyodbc
from contextlib import contextmanager

# --- Configuración de la Conexión a SQL Server ---
# Lee las variables de entorno que coinciden con el archivo .env
DB_SERVER = os.environ.get('SQL_SERVER_HOST')
DB_PORT = os.environ.get('SQL_SERVER_PORT')
DB_DATABASE = os.environ.get('SQL_SERVER_DATABASE')
DB_USERNAME = os.environ.get('SQL_SERVER_USER')
DB_PASSWORD = os.environ.get('SQL_SERVER_PASSWORD')

# --- Función de ayuda para obtener una conexión de BD ---
@contextmanager
def get_db():
    """
    Esta función crea una nueva conexión a la base de datos para cada petición,
    la entrega al endpoint y se asegura de que se cierre correctamente al final.
    """
    conn = None
    # Validar que todas las variables de entorno necesarias están presentes
    if not all([DB_SERVER, DB_PORT, DB_DATABASE, DB_USERNAME, DB_PASSWORD]):
        raise ValueError("Una o más variables de entorno para la base de datos no están configuradas.")
        
    try:
        # Construir la cadena de conexión para pyodbc
        conn_str = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={DB_SERVER},{DB_PORT};"
            f"DATABASE={DB_DATABASE};"
            f"UID={DB_USERNAME};"
            f"PWD={DB_PASSWORD};"
            f"TrustServerCertificate=yes;"
        )
        conn = pyodbc.connect(conn_str)
        yield conn
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Error de conexión a la base de datos: {sqlstate}")
        raise
    finally:
        if conn:
            conn.close()

# --- CONEXIÓN A SYBASE (ALTERNATIVA) ---
# Descomentar este bloque para usar Sybase y comentar el de SQL Server
# NOTA: Asegúrate de descomentar la instalación de FreeTDS en el Dockerfile y actualizar el .env
# server = os.getenv('SYBASE_HOST')
# database = os.getenv('SYBASE_DB')
# username = os.getenv('SYBASE_USER')
# password = os.getenv('SYBASE_PASSWORD')
# port = os.getenv('SYBASE_PORT', '5000') # Puerto por defecto de Sybase
# driver = '{FreeTDS}'
# connection_string = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password};TDS_Version=5.0;'
# db_connection = pyodbc.connect(connection_string)
# print("Conexión a Sybase establecida exitosamente.")
