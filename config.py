"""Archivo de configuración de la aplicación
Debes descomentar la línea de la base de datos que deseas usar
Debes comentar la línea de la base de datos que no deseas usar
En las variables como: SYBASE_HOST, SYBASE_PORT, SYBASE_DATABASE, SYBASE_USER, SYBASE_PASSWORD puedes agregar en el segundo parámetro el valor de la variable de entorno
Por ejemplo: SYBASE_HOST = os.environ.get('SYBASE_HOST', 'localhost')
El segundo parámetro es el valor por defecto si no se encuentra la variable de entorno en el archivo .env
SYBASE_CONNECTION_STRING es la cadena de conexión para Sybase; mssql+pyodbc son los drivers que se usan para conectarse a Sybase y ?driver=FreeTDS es para que use el driver FreeTDS
SQL_SERVER_CONNECTION_STRING es la cadena de conexión para SQL Server """

import os

class Config:
    """
    Clase de configuración que contiene las variables de entorno necesarias
    """
    # Configuración de SQL Server
    # SQL_SERVER_HOST = os.environ.get('SQL_SERVER_HOST', 'localhost')
    # SQL_SERVER_PORT = os.environ.get('SQL_SERVER_PORT', '1433')
    # SQL_SERVER_DATABASE = os.environ.get('SQL_SERVER_DATABASE', 'mi_base_de_datos')
    # SQL_SERVER_USER = os.environ.get('SQL_SERVER_USER', 'sa')
    # SQL_SERVER_PASSWORD = os.environ.get('SQL_SERVER_PASSWORD', '')
    
    # Cadena de conexión para SQL Server
    # SQL_SERVER_CONNECTION_STRING = f"mssql+pyodbc://{SQL_SERVER_USER}:{SQL_SERVER_PASSWORD}@{SQL_SERVER_HOST}:{SQL_SERVER_PORT}/{SQL_SERVER_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"

    # Configuración de JWT
    # JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'tu-clave-secreta-de-jwt')

    # Configuración de Sybase
    SYBASE_HOST = os.environ.get('SYBASE_HOST', 'localhost') #el segundo parametro es el valor por defecto si no se encuentra la variable de entorno en el archivo .env
    SYBASE_PORT = os.environ.get('SYBASE_PORT', '5000')
    SYBASE_DATABASE = os.environ.get('SYBASE_DATABASE', 'PruebaMicroServicios')
    SYBASE_USER = os.environ.get('SYBASE_USER', 'sa')
    SYBASE_PASSWORD = os.environ.get('SYBASE_PASSWORD', '12345678')
    
    # Cadena de conexión para Sybase
    SYBASE_CONNECTION_STRING = f"mssql+pyodbc://{SYBASE_USER}:{SYBASE_PASSWORD}@{SYBASE_HOST}:{SYBASE_PORT}/{SYBASE_DATABASE}?driver=FreeTDS"
    