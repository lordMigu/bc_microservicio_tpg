# Microservicio de Autenticación y Consultas

Este microservicio proporciona una API RESTful para consultar información de contenedores, BLs y otros datos logísticos, compatible con SAP ASE 16.1 y SQL Server.

## Tabla de Contenidos
1. [Configuración de Base de Datos](#1-configuración-de-base-de-datos)
2. [Variables de Entorno](#2-variables-de-entorno)
3. [Procedimientos Almacenados](#3-procedimientos-almacenados)
4. [Despliegue con Docker](#4-despliegue-con-docker)
5. [Pruebas de la API](#5-pruebas-de-la-api)
6. [Desarrollo Local](#6-desarrollo-local)
7. [Configuración de Base de Datos](#7-configuración-de-base-de-datos)

## Tecnologías Utilizadas

- **Backend**: Python 3.11 con Flask
- **Base de Datos**: SAP ASE 16.1 o SQL Server
- **Driver**: FreeTDS con soporte para TDS 4.2 (SAP ASE) / ODBC Driver 17 for SQL Server
- **Contenedorización**: Docker y Docker Compose
- **ODBC**: unixODBC
- **Logging**: Loguru

## Configuración del Entorno

### 1. Configuración de Base de Datos

Para configurar la base de datos, siga estos pasos:

1. **Seleccione su gestor de base de datos** y descomente la línea correspondiente en los siguientes archivos:
   - `.env`
   - `docker-compose.yml`
   - `config.py`
   - `Dockerfile`

2. Comente las líneas de los otros gestores de base de datos que no vaya a utilizar.

### 2. Variables de Entorno

Cree un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# Configuración de la aplicación
FLASK_APP=app.py
FLASK_ENV=development

# Configuración de SQL Server (descomentada por defecto)
SQL_SERVER_HOST=localhost
SQL_SERVER_PORT=1433
SQL_SERVER_DATABASE=mi_base_de_datos
SQL_SERVER_USER=sa
SQL_SERVER_PASSWORD=

# Configuración de Sybase (comentada por defecto)
# SYBASE_HOST=localhost
# SYBASE_PORT=5000
# SYBASE_DATABASE=PruebaMicroServicios
# SYBASE_USER=sa
# SYBASE_PASSWORD=12345678

# Configuración JWT (opcional)
# JWT_SECRET_KEY=tu-clave-secreta-de-jwt
```

### 3. Configuración de Stored Procedures

Asegúrese de que los stored procedures estén creados en su base de datos con los parámetros exactos. Los parámetros deben coincidir exactamente en nombre, tipo y orden con los definidos en los procedimientos almacenados.

Ejemplo para SQL Server:
```sql
CREATE PROCEDURE sp_autenticar_usuario
    @usuario NVARCHAR(100),
    @contrasena NVARCHAR(255)
AS
BEGIN
    -- Lógica del procedimiento
END
```

### 4. Configuración de Docker

Asegúrese de que el archivo `Dockerfile` tenga la configuración correcta para su base de datos. Descomente las líneas correspondientes a su gestor de base de datos y comente las demás.

## Requisitos Previos

- **Docker y Docker Compose**: Para construir y ejecutar la aplicación en un contenedor.
- **Cliente SQL**: Una herramienta como SAP ASE 16 o SQL Server Management Studio. (Dependiendo de la base de datos que desees usar debe comentar la línea de la base de datos que no deseas usar en los archivos .env, docker-compose.yml, config.py y Dockerfile y descomentar la línea de la base de datos que deseas usar)
- **Postman o similar**: Para probar los endpoints de la API.

---

## Puesta en Marcha

### 1. Configuración Inicial

1. **Clonar el repositorio** (si aún no lo ha hecho):
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd auth_login_docker-main
   ```

2. **Configurar el archivo .env** como se describe en la sección de Variables de Entorno.

### 2. Despliegue con Docker

1. **Construir y ejecutar los contenedores**:
   ```bash
   docker-compose up --build
   ```

2. **Verificar que el contenedor esté en ejecución**:
   ```bash
   docker ps
   ```

3. **Acceder a la aplicación**:
   Abra su navegador y visite:
   ```
   http://localhost:5000
   ```

### 3. Pruebas de la API

Puede probar los endpoints usando cURL o Postman:

```bash
# Ejemplo de consumo
endpoint [GET]: http://0.0.0.0:5000/consulta_info/info_bl?numero_bl=HLCUSS524I210674

```

## Desarrollo Local con Entorno Virtual (venv)

Si prefiere ejecutar la aplicación sin Docker, siga estos pasos:

1. **Crear y activar el entorno virtual**:
   ```bash
   # Windows
   python -m venv .entorno-virtual
   .\.entorno-virtual\Scripts\activate

   # Linux/Mac
   python3 -m venv .entorno-virtual
   source .entorno-virtual/bin/activate
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**:
   Asegúrese de que el archivo `.env` esté configurado correctamente.

4. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

5. **Acceder a la aplicación**:
   ```
   http://localhost:5000
   ```

## Solución de Problemas Comunes

- **Error de conexión a la base de datos**: Verifique que las credenciales en `.env` sean correctas y que el servidor de base de datos esté en ejecución.
- **Problemas con Docker**: Asegúrese de que Docker Desktop esté en ejecución y tenga suficientes recursos asignados.
- **Errores de autenticación**: Verifique que los parámetros de los stored procedures coincidan exactamente con los esperados por la aplicación.

---

## Consumir la API con Postman

### Especificaciones Técnicas

- **Base de Datos**: SAP ASE 16.1
- **Backend**: Python 3.11 con Flask
- **Driver**: FreeTDS con soporte para TDS 4.2
- **Interfaz**: ODBC a través de unixODBC

### Configuración de Conexión a SAP ASE 16.1

La conexión a SAP ASE 16.1 se realiza a través de FreeTDS con la siguiente configuración:

```ini
[SAPASE_HOST]
    host = host.docker.internal
    port = 5000
    tds version = 4.2
```

### Requisitos del Sistema

- Docker 20.10+
- Docker Compose 2.0+
- Acceso a un servidor SAP ASE 16.1
- Mínimo 2GB de RAM asignados a Docker