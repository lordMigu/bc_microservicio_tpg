# Archivo de configuración de la aplicación

import os

class Config:
    """
    Clase de configuración que contiene las variables de entorno necesarias
    """
    # Configuración de SQL Server
    SQL_SERVER_HOST = os.environ.get('SQL_SERVER_HOST', 'localhost')
    SQL_SERVER_PORT = os.environ.get('SQL_SERVER_PORT', '1433')
    SQL_SERVER_DATABASE = os.environ.get('SQL_SERVER_DATABASE', 'mi_base_de_datos')
    SQL_SERVER_USER = os.environ.get('SQL_SERVER_USER', 'sa')
    SQL_SERVER_PASSWORD = os.environ.get('SQL_SERVER_PASSWORD', '')
    
    # Cadena de conexión para SQL Server
    SQL_SERVER_CONNECTION_STRING = f"mssql+pyodbc://{SQL_SERVER_USER}:{SQL_SERVER_PASSWORD}@{SQL_SERVER_HOST}:{SQL_SERVER_PORT}/{SQL_SERVER_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"

    # Configuración de JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'tu-clave-secreta-de-jwt')