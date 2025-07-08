import os
import pyodbc
from contextlib import contextmanager

# Proporciona una conexión a la base de datos. Actualmente configurado para Sybase.
# Para cambiar a SQL Server, comenta la función get_db() de Sybase y descomenta la de SQL Server.

# --- CONEXIÓN A SYBASE (ACTIVA) ---
@contextmanager
def get_db():
    """
    Crea y gestiona una conexión a la base de datos Sybase.
    """
    conn = None
    db_name = os.environ.get('SYBASE_DATABASE')
    db_user = os.environ.get('SYBASE_USER')
    db_password = os.environ.get('SYBASE_PASSWORD')

    if not all([db_name, db_user, db_password]):
        raise ValueError("Faltan variables de entorno para la conexión a Sybase.")
    
    try:
        # Usamos la configuración directa de ODBC
        conn_str = (
            f"DRIVER={{FreeTDS}};"
            f"SERVER=host.docker.internal,5000;"
            f"DATABASE={db_name};"
            f"UID={db_user};"
            f"PWD={db_password};"
            f"TDS_Version=4.2;"
        )
        print(f"Intentando conectar con: {conn_str}")  # Para depuración
        conn = pyodbc.connect(conn_str)
        yield conn
    except pyodbc.Error as ex:
        print(f"Error de conexión a Sybase: {ex.args[0]}")
        raise
    finally:
        if conn:
            conn.close()

# --- CONEXIÓN A SQL SERVER (COMENTADA) ---
# @contextmanager
# def get_db():
#     """
#     Crea y gestiona una conexión a la base de datos SQL Server.
#     """
#     conn = None
#     db_server = os.environ.get('SQL_SERVER_HOST')
#     db_port = os.environ.get('SQL_SERVER_PORT')
#     db_database = os.environ.get('SQL_SERVER_DATABASE')
#     db_username = os.environ.get('SQL_SERVER_USER')
#     db_password = os.environ.get('SQL_SERVER_PASSWORD')

#     if not all([db_server, db_port, db_database, db_username, db_password]):
#         raise ValueError("Faltan variables de entorno para la conexión a SQL Server.")
        
#     try:
#         conn_str = (
#             f"DRIVER={{ODBC Driver 18 for SQL Server}};"
#             f"SERVER={db_server},{db_port};"
#             f"DATABASE={db_database};"
#             f"UID={db_username};"
#             f"PWD={db_password};"
#             f"TrustServerCertificate=yes;"
#         )
#         conn = pyodbc.connect(conn_str)
#         yield conn
#     except pyodbc.Error as ex:
#         print(f"Error de conexión a SQL Server: {ex.args[0]}")
#         raise
#     finally:
#         if conn:
#             conn.close()
