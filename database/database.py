import os
import pytds
from contextlib import contextmanager

# --- Configuración de la Conexión a SQL Server ---
DB_SERVER = os.environ.get('DB_SERVER', 'sqlserver')
DB_PORT = os.environ.get('DB_PORT', '1433')
DB_DATABASE = os.environ.get('DB_DATABASE', 'PruebaMicroServicios')
DB_USERNAME = os.environ.get('SQL_SERVER_USER', 'sa')
DB_PASSWORD = os.environ.get('SQL_SERVER_PASSWORD', 'YourStrongPassword@2025')

# --- Función de ayuda para obtener una conexión de BD ---
@contextmanager
def get_db():
    """
    Esta función crea una nueva conexión a la base de datos para cada petición,
    la entrega al endpoint y se asegura de que se cierre correctamente al final.
    """
    conn = None
    try:
        conn = pytds.connect(
            host=DB_SERVER,
            port=int(DB_PORT),
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_DATABASE,
            tds_version='7.2'
        )
        yield conn
    finally:
        if conn:
            conn.close()
