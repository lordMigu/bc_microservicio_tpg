# Microservicio de Autenticación y Consulta

Este microservicio expone una API REST para consumir los siguientes servicios:

- Consultas
- Trazabilidad
- Servicios complementarios
- Estadísticas
- Notificaciones
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
#JWT es opcional
JWT_SECRET_KEY=una_clave_secreta_muy_segura
```

**Para Sybase:**
```env
SYBASE_HOST=host.docker.internal
SYBASE_DB=NombreDeTuBD
SYBASE_USER=tu_usuario
SYBASE_PASSWORD=tu_contraseña
SYBASE_PORT=5000
#JWT es opcional
JWT_SECRET_KEY=una_clave_secreta_muy_segura
```

### 3. Construir y Ejecutar el Contenedor

Una vez configurado los archivos .env, docker-compose.yml, config.py y Dockerfile, ejecuta el siguiente comando:

```bash
docker-compose up --build
```

Este comando construirá la imagen de Docker y levantará el contenedor. La aplicación estará disponible en `http://localhost:5000`.

---

## Consumir la API con Postman
# Para las rutas de query debes usar los siguientes endpoints de la carpeta /query con los siguientes parámetros que coinciden con la base de datos de prueba:

1. /query/booking/{booking_id}

Parámetros:
- booking_id: BK-001
- ruc_cliente: 12345678901

2. /query/container/import/{ruc_cliente}/{fecha_inicio}/{fecha_fin}

Parámetros:
- ruc_cliente: 12345678901
- fecha_inicio: 2023-01-01
- fecha_fin: 2023-12-31

3. /query/container/export/{ruc_cliente}/{fecha_inicio}/{fecha_fin}

Parámetros:
- ruc_cliente: 12345678901
- fecha_inicio: 2023-01-01
- fecha_fin: 2023-12-31   

4. /query/bl-loose-cargo/{numero_bl}/{ruc_cliente}

Parámetros:
- numero_bl: BL-CS-001
- ruc_cliente: 12345678901

5. /query/aforo/bl/{numero_bl}/{ruc_cliente}

Parámetros:
- numero_bl: BL-CS-001
- ruc_cliente: 12345678901

6. /query/aforo/container/{contenedor_id}/{ruc_cliente}

Parámetros:
- contenedor_id: CONT-IMPO-001
- ruc_cliente: 12345678901  

7. /query/inspection/booking/{booking_id}/{ruc_cliente}

Parámetros:
- booking_id: BK-001
- ruc_cliente: 12345678901