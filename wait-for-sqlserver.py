import pytds
import time

MAX_RETRIES = 30

def wait_for_sqlserver():
    print("Waiting for SQL Server to be ready...")

    for attempt in range(MAX_RETRIES):
        try:
            # Intenta conectarse usando pytds
            conn = pytds.connect(
                host='172.18.0.2',
                port=1433,
                user='sa',
                password='YourStrongPassword@2025',
                database='master',
                tds_version='7.2'
            )
            
            # Primero verifica si la base de datos existe
            with conn.cursor() as cursor:
                cursor.execute("SELECT name FROM sys.databases WHERE name = 'PruebaMicroServicios'")
                result = cursor.fetchone()
                if not result:
                    print("Base de datos PruebaMicroServicios no existe. Creando...")
                    cursor.execute("CREATE DATABASE PruebaMicroServicios")
                    conn.commit()
                    print("Base de datos creada exitosamente")
            
            # Intenta conectarse a la base de datos específica
            conn = pytds.connect(
                host='172.18.0.2',
                port=1433,
                user='sa',
                password='YourStrongPassword@2025',
                database='PruebaMicroServicios',
                tds_version='7.2'
            )
            
            # Intenta ejecutar una consulta simple para verificar la conexión
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()
            print("SQL Server está listo!")
            return True
        except Exception as e:
            print(f"SQL Server not ready yet. Retrying... ({MAX_RETRIES - attempt} attempts left)")
            print(f"Error: {str(e)}")
            time.sleep(2)
    
    print("No se pudo conectar a SQL Server después de varios intentos")
    return False

if __name__ == "__main__":
    wait_for_sqlserver()
