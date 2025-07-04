# Sistema de Autenticación JWT con Conexión a Base de Datos

Este proyecto es una aplicación Flask que implementa un sistema de autenticación usando JWT (JSON Web Tokens) y está configurado para conectarse a **SQL Server**, con una opción para migrar a **Sybase**.

---

## Requisitos Previos

- **Docker Desktop** (o Docker Engine)
- **Docker Compose**
- **Git** (opcional, para clonar)

---

## Instalación y Ejecución (con SQL Server)

1.  **Configurar variables de entorno**:
    Crea un archivo `.env` con las credenciales de SQL Server:
    ```bash
    SQL_SERVER_HOST=host.docker.internal # O la IP del host
    SQL_DATABASE=PruebaMicroServicios
    SQL_USER=tu_usuario
    SQL_PASSWORD=tu_contraseña
    ```

2.  **Construir y levantar los servicios**:
    ```bash
    docker-compose up --build
    ```

La aplicación estará disponible en `http://localhost:5000`.

---

## Gestión de la Imagen en Docker Hub y Ejecución

Esta sección explica cómo subir la imagen de la aplicación a Docker Hub y cómo ejecutarla directamente, pasando las variables de entorno desde la terminal.

### 1. Subir la imagen a Docker Hub

Para compartir la imagen de tu aplicación, puedes subirla a un registro como Docker Hub.

**a. Inicia sesión en Docker Hub:**
```bash
docker login
```
Introduce tu nombre de usuario y contraseña de Docker Hub.

**b. Construye y etiqueta la imagen:**
Primero, construye la imagen con `docker-compose` y luego etiquétala con el formato de Docker Hub.

```bash
# 1. Construye la imagen usando docker-compose
docker-compose build

# 2. Etiqueta la imagen (reemplaza <usuario_hub> con tu usuario de Docker Hub)
# El nombre 'auth_login_docker-main_app' se basa en '<nombre_directorio>_<nombre_servicio>'
docker tag auth_login_docker-main_app <usuario_hub>/auth-app:1.0
```

**c. Sube la imagen:**
```bash
docker push <usuario_hub>/auth-app:1.0
```

### 2. Bajar y ejecutar la imagen desde Docker Hub

Una vez que la imagen está en Docker Hub, cualquiera puede bajarla y ejecutarla sin necesidad del código fuente.

**a. Baja la imagen:**
```bash
docker pull <usuario_hub>/auth-app:1.0
```

**b. Ejecuta el contenedor:**
Para ejecutar el contenedor, debes proporcionar las variables de entorno requeridas usando la opción `-e`.

```bash
docker run -d -p 5000:5000 \
  -e SQL_SERVER_HOST='<ip_o_host_de_tu_db>' \
  -e SQL_DATABASE='PruebaMicroServicios' \
  -e SQL_USER='tu_usuario_db' \
  -e SQL_PASSWORD='tu_password_db' \
  -e JWT_SECRET_KEY='tu_clave_secreta_para_jwt' \
  --name mi-auth-app \
  <usuario_hub>/auth-app:1.0
```

**Explicación de los parámetros:**
-   `-d`: Ejecuta el contenedor en segundo plano.
-   `-p 5000:5000`: Mapea el puerto 5000 del host al puerto 5000 del contenedor.
-   `-e VARIABLE='valor'`: Establece una variable de entorno.
-   `--name mi-auth-app`: Asigna un nombre al contenedor para identificarlo fácilmente.

---

## Cambio de Base de Datos (de SQL Server a Sybase)

El proyecto está preparado para cambiar la conexión a Sybase. Sigue estos pasos:

### 1. Modificar el `Dockerfile`

Cambia el driver de la base de datos comentando el de SQL Server y descomentando el de Sybase (FreeTDS).

```dockerfile
# --- DRIVER PARA SQL SERVER (ACTUAL) ---
# Comenta estas líneas para desactivar
# RUN apt-get update && apt-get install -y unixodbc-dev
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# ... (resto de líneas de msodbcsql18)

# --- DRIVER PARA SYBASE (ALTERNATIVA) ---
# Descomenta esta línea para activar
RUN apt-get update && apt-get install -y freetds-dev freetds-bin unixodbc-dev
```

### 2. Modificar `database/database.py`

Ajusta el bloque de código que establece la conexión.

```python
# --- CONEXIÓN A SQL SERVER (ACTUAL) ---
# Comenta todo este bloque para desactivar
# server = os.getenv('SQL_SERVER_HOST')
# ...

# --- CONEXIÓN A SYBASE (ALTERNATIVA) ---
# Descomenta todo este bloque para activar
server = os.getenv('SYBASE_HOST')
database = os.getenv('SYBASE_DB')
username = os.getenv('SYBASE_USER')
password = os.getenv('SYBASE_PASSWORD')
port = os.getenv('SYBASE_PORT', '5000')
driver = '{FreeTDS}'
connection_string = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password};TDS_Version=5.0;'
db_connection = pyodbc.connect(connection_string)
print("Conexión a Sybase establecida exitosamente.")
```

### 3. Actualizar el archivo `.env`

Asegúrate de que tu archivo `.env` contenga las variables para Sybase:

```bash
# Variables para Sybase
SYBASE_HOST=tu_host_sybase
SYBASE_DB=tu_db_sybase
SYBASE_USER=tu_usuario_sybase
SYBASE_PASSWORD=tu_password_sybase
SYBASE_PORT=5000 # O el puerto que corresponda
```

### 4. Reconstruir la imagen de Docker

Finalmente, reconstruye la imagen para aplicar los cambios:

```bash
docker-compose up --build
```
- **GET `http://localhost:5000/auth/protected`**
  - **Headers**:
    ```
    Authorization: Bearer eyJhbGciOiJIUzI1NiIsInT5cCI6IkpXVCJ9...
    ```
  - **Respuesta**:
    ```json
    {
        "message": "Acceso concedido"
    }
    ```

### Endpoints de Consulta (`/query`)

Todos los endpoints de consulta requieren autenticación vía JWT. El `ruc_cliente` se obtiene del token.

#### 1. Consulta de Booking
- **GET `/query/booking`**
  - **Parámetros (Query String):**
    - `booking_id`: El ID del booking a consultar.
  - **Request:**
    ```bash
    curl -X GET 'http://localhost:5000/query/booking?booking_id=BK-001' \
      -H "Authorization: Bearer <token>"
    ```
  - **Response (200 OK):**
    ```json
    {
        "booking_id": "BK-001",
        "buque": "Buque Ejemplo",
        "contenedores": "CONT1, CONT2",
        "dae": "DAE-001",
        "estados": "Activo",
        "id": 1,
        "inspecciones": "Ninguna",
        "mrn": "MRN-123",
        "puerto_destino": "Puerto Destino A",
        "ruc_cliente": "12345678901",
        "tipo_carga": "Carga General"
    }
    ```

#### 2. Consulta de Contenedor de Importación
- **GET `/query/container/import`**
  - **Parámetros (Query String):**
    - `numero_contenedor`: El número del contenedor.
  - **Request:**
    ```bash
    curl -X GET 'http://localhost:5000/query/container/import?numero_contenedor=CONT-IMPO-001' \
      -H "Authorization: Bearer <token>"
    ```
  - **Response (200 OK):**
    ```json
    {
        "aforos": "Aforo Físico",
        "almacenaje": "Bodega 5",
        "despacho": "Despachado",
        "dress": "DRESS-01",
        "eventos": "Llegada, Descarga",
        "fecha_llegada": "Wed, 03 Jul 2024 00:26:30 GMT",
        "mrn": "MRN-456",
        "peso": 1500.50,
        "puerto": "Puerto Origen B"
    }
    ```

#### 3. Consulta de Contenedor de Exportación
- **GET `/query/container/export`**
  - **Parámetros (Query String):**
    - `numero_contenedor`: El número del contenedor.
  - **Request:**
    ```bash
    curl -X GET 'http://localhost:5000/query/container/export?numero_contenedor=CONT-EXPO-001' \
      -H "Authorization: Bearer <token>"
    ```
  - **Response (200 OK):**
    ```json
    {
        "conexiones": "Conexión Eléctrica",
        "dae": "DAE-002",
        "disv": "DISV-02",
        "estados": "Listo para embarque",
        "fecha_embarque": "Wed, 03 Jul 2024 00:26:30 GMT",
        "roleo": "No"
    }
    ```

#### 4. Consulta de BL de Carga Suelta
- **GET `/query/bl-loose-cargo`**
  - **Parámetros (Query String):**
    - `numero_bl`: El número del Bill of Lading.
  - **Request:**
    ```bash
    curl -X GET 'http://localhost:5000/query/bl-loose-cargo?numero_bl=BL-CS-001' \
      -H "Authorization: Bearer <token>"
    ```
  - **Response (200 OK):**
    ```json
    {
        "almacenaje": "Patio 3",
        "bultos": 50,
        "contenedor_desconsolidacion": "CONT-DESC-01",
        "despacho": "En proceso",
        "peso": 500.75,
        "tarja": "TARJA-123"
    }
    ```

#### 5. Consulta de Aforos
- **Por BL:** `GET /query/aforo/bl?numero_bl=<numero_bl>`
- **Por Contenedor:** `GET /query/aforo/container?numero_contenedor=<numero_contenedor>`
  - **Response (200 OK):**
    ```json
    [
        {
            "estado": "Programado",
            "fecha_programacion": "Wed, 03 Jul 2024 00:26:30 GMT",
            "id": 1,
            "numero_bl": "BL-CS-001",
            "numero_contenedor": null,
            "ruc_cliente": "12345678901",
            "tipo_aforo": "Aforo Físico"
        }
    ]
    ```

#### 6. Consulta de Inspecciones
- **Por Booking:** `GET /query/inspection/booking?booking_id=<booking_id>`
- **Por Contenedor:** `GET /query/inspection/container?numero_contenedor=<numero_contenedor>`
  - **Response (200 OK):**
    ```json
    [
        {
            "booking_id": "BK-001",
            "estado": "Solicitado",
            "fecha_inspeccion": "Wed, 03 Jul 2024 00:26:30 GMT",
            "id": 1,
            "numero_contenedor": null,
            "requerimiento": "Inspección de Antinarcóticos",
            "ruc_cliente": "12345678901"
        }
    ]
    ```

#### 7. Consulta de Tarjas (Carga Suelta)
- **GET `/query/tally`**
  - **Parámetros (Query String):**
    - `numero_bl`: El número del Bill of Lading.
  - **Request:**
    ```bash
    curl -X GET 'http://localhost:5000/query/tally?numero_bl=BL-CS-001' \
      -H "Authorization: Bearer <token>"
    ```
  - **Response (200 OK):**
    ```json
    [
        {
            "bultos": 10,
            "descripcion": "Cajas de repuestos",
            "id": 1,
            "numero_bl": "BL-CS-001",
            "numero_tarja": "TARJA-CS-001",
            "peso": 100.50,
            "ruc_cliente": "12345678901"
        }
    ]
    ```

### Ejemplo de Uso con un Usuario Existente

Para probar la aplicación, puedes usar el siguiente usuario de prueba:

1. **Login**:
```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "importador.activo@empresa.com", "password": "hash_de_prueba_123"}'
```

2. **Luego usa el token obtenido para acceder al recurso protegido**:
```bash
curl -X GET http://localhost:5000/protected \
  -H "Authorization: Bearer <token_obtenido_anteriormente>"
```

### Notas sobre Seguridad
- La contraseña debe cumplir con los requisitos de seguridad mínimos
- El token JWT tiene un tiempo de expiración
- Los endpoints protegidos requieren autenticación
- Se recomienda usar HTTPS en producción

## Parámetros de Docker Compose

El archivo `docker-compose.yml` configura dos servicios principales:

1. **app**: La aplicación Flask principal
   - Puerto: 5000
   - Variables de entorno para conexión a SQL Server

2. **sqlserver**: Servicio de SQL Server
   - Puerto: 1433
   - Base de datos: mi_base_de_datos
   - Usuario: sa
   - Contraseña: TuPasswordSeguro123

## Parar los servicios

Para detener los servicios, usa:
```bash
docker-compose down
```

## Notas importantes

- Asegúrate de tener suficiente espacio en disco para los contenedores
- La contraseña de SQL Server debe cumplir con los requisitos de seguridad de SQL Server
- Los logs de la aplicación se pueden ver con:
```bash
docker-compose logs -f app
```

## Problemas comunes

1. Si hay problemas con la conexión a SQL Server:
   - Verifica que la contraseña cumple con los requisitos de seguridad
   - Asegúrate de que el servicio de SQL Server está corriendo
   - Verifica los logs para más detalles del error
* `DB_PASSWORD_SQL`: Contraseña del usuario SQL
* `JWT_SECRET_KEY`: Clave secreta para firmar tokens JWT
* `DB_DRIVER`: Controlador ODBC a utilizar

---

## Verificación y Pruebas

### Verificar el Estado del Contenedor

```bash
docker ps
```

Asegúrate de que el contenedor `tpg-microservice-app` esté en estado `Up`.

### Revisar los Logs

```bash
docker logs -f tpg-microservice-app
```

Busca mensajes como:

* `Sistema de logging inicializado.`
* `Usando autenticación de SQL Server.`

> Si hay errores de conexión, revisa tus variables de entorno y configuración de SQL Server.

---

## Probar el Microservicio

Usa una herramienta HTTP (Postman, Insomnia o `curl`) para enviar una petición.

### Ejemplo: Login

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"email": "importador.activo@empresa.com", "password": "hash_de_prueba_123"}' \
     http://localhost:8000/auth/login
```

> Asegúrate de usar credenciales válidas presentes en la tabla `Usuarios`.

---

✅ Si recibes una respuesta con un token JWT, ¡el microservicio está funcionando correctamente!

```

¿Deseas también una versión en PDF o un archivo `.md` listo para descargar?
```