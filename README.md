# Microservicio de Autenticación y Consultas

Este es un microservicio desarrollado con Flask que proporciona autenticación y consultas a una base de datos SAP ASE 16.1.

## Tecnologías Utilizadas

- **Backend**: Python 3.11 con Flask
- **Base de Datos**: SAP ASE 16.1
- **Driver**: FreeTDS con soporte para TDS 4.2
- **Contenedorización**: Docker
- **ODBC**: unixODBC

## Configuración del Entorno

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# Configuración de la aplicación
FLASK_APP=app.py
FLASK_ENV=development

# Configuración de SAP ASE 16.1
SYBASE_DATABASE=PruebaMicroServicios
SYBASE_USER=sa
SYBASE_PASSWORD=12345678
SYBASE_PORT=5000
```
- Información financiera

## Requisitos Previos

- **Docker y Docker Compose**: Para construir y ejecutar la aplicación en un contenedor.
- **Cliente SQL**: Una herramienta como SAP ASE 16 o SQL Server Management Studio. (Dependiendo de la base de datos que desees usar debe comentar la línea de la base de datos que no deseas usar en los archivos .env, docker-compose.yml, config.py y Dockerfile y descomentar la línea de la base de datos que deseas usar)
- **Postman o similar**: Para probar los endpoints de la API.

---

## Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el microservicio en tu entorno local.

### 1. Configurar la Base de Datos

Antes de levantar la aplicación, necesitas una base de datos funcionando y con la estructura y datos necesarios.

1.  **Inicia tu instancia de base de datos** (SQL Server o Sybase).
2.  **Ejecuta los scripts SQL**: Conéctate a tu base de datos usando un cliente SQL y ejecuta los siguientes scripts del directorio `/sql` en orden. Asegúrate de usar los scripts del directorio correspondiente a tu motor de base de datos (`/mssql` o `/sybase`).

    -   `01_schema.sql`: Crea todas las tablas y relaciones.
    -   `02_data.sql`: Inserta los datos iniciales (ej. usuarios de prueba).
    -   `03_procedures.sql`: Crea los procedimientos almacenados que usa la API.

### 2. Configurar Variables de Entorno

Crea un archivo llamado `.env` en la raíz del proyecto. Este archivo contendrá las credenciales y configuraciones para que la aplicación se conecte a la base de datos.

**Para SQL Server:**
```env
SQL_SERVER_HOST=host.docker.internal # O la IP de tu host si Docker no puede resolverlo
SQL_DATABASE=NombreDeTuBD
SQL_USER=tu_usuario
SQL_PASSWORD=tu_contraseña
```

**Para Sybase:**
```env
SYBASE_HOST=host.docker.internal
SYBASE_DB=NombreDeTuBD
SYBASE_USER=tu_usuario
SYBASE_PASSWORD=tu_contraseña
SYBASE_PORT=5000
```

### 3. Construir y Ejecutar el Contenedor

Una vez configurado los archivos .env, docker-compose.yml, config.py y Dockerfile, ejecuta el siguiente comando:

```bash
docker-compose up --build
```

Este comando construirá la imagen de Docker y levantará el contenedor. La aplicación estará disponible en `http://localhost:5000`.

---

## Consumir la API con Postman

### Especificaciones Técnicas

- **Base de Datos**: SAP ASE 16.1
- **Backend**: Python 3.11 con Flask
- **Driver**: FreeTDS con soporte para TDS 4.2
- **Interfaz**: ODBC a través de unixODBC

### Tabla de Endpoints

| # | Método | Endpoint | Parámetros | Valores de Ejemplo |
|---|--------|----------|------------|-------------------|
| 1 | GET | `/query/booking/{booking_id}` | `booking_id`: Número de booking<br>`ruc_cliente`: RUC del cliente | `BK-001`<br>`12345678901` |
| 2 | GET | `/query/container/import` | `numero_contenedor`: Número de contenedor<br>`ruc_cliente`: RUC del cliente | `CONT-IMPO-001`<br>`12345678901` |
| 3 | GET | `/query/container/export/{ruc_cliente}/{fecha_inicio}/{fecha_fin}` | `ruc_cliente`: RUC del cliente<br>`fecha_inicio`: Fecha de inicio (YYYY-MM-DD)<br>`fecha_fin`: Fecha de fin (YYYY-MM-DD) | `12345678901`<br>`2023-01-01`<br>`2023-12-31` |
| 4 | GET | `/query/bl-loose-cargo/{numero_bl}/{ruc_cliente}` | `numero_bl`: Número de BL<br>`ruc_cliente`: RUC del cliente | `BL-CS-001`<br>`12345678901` |
| 5 | GET | `/query/aforo/bl/{numero_bl}/{ruc_cliente}` | `numero_bl`: Número de BL<br>`ruc_cliente`: RUC del cliente | `BL-CS-001`<br>`12345678901` |
| 6 | GET | `/query/aforo/container/{contenedor_id}/{ruc_cliente}` | `contenedor_id`: Número de contenedor<br>`ruc_cliente`: RUC del cliente | `CONT-IMPO-001`<br>`12345678901` |
| 7 | GET | `/query/inspection/booking/{booking_id}/{ruc_cliente}` | `booking_id`: Número de booking<br>`ruc_cliente`: RUC del cliente | `BK-001`<br>`12345678901` |

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