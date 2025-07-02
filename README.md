# Sistema de Autenticación JWT con SQL Server

Este proyecto es una aplicación Flask que implementa un sistema de autenticación usando JWT (JSON Web Tokens) y SQL Server como base de datos.

---

## Requisitos Previos

Para levantar y ejecutar este servicio, necesitarás:

- **Docker Desktop** (o Docker Engine): Para ejecutar los servicios en contenedores.
- **Docker Compose**: Para gestionar múltiples contenedores.
- **Git**: Para clonar el repositorio (si lo obtienes desde un repositorio).

---

## Estructura del Proyecto

```

auth_login_docker-main/
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md

````

---

## Preparación de la Base de Datos SQL Server

## Instalación y Ejecución

Para ejecutar la aplicación usando Docker Compose, no es necesario clonar el repositorio. Sin embargo, si deseas modificar el código fuente o desarrollar nuevas funcionalidades, sigue estos pasos:

1. Clona el repositorio:
```bash
git clone [url_del_repositorio]
cd auth_login_docker-main
```

2. Configura las variables de entorno:
Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
```bash
SQL_SERVER_HOST=sqlserver
SQL_SERVER_PORT=1433
SQL_SERVER_DATABASE=mi_base_de_datos
SQL_SERVER_USER=sa
SQL_SERVER_PASSWORD=TuPasswordSeguro123
```

3. Construye y levanta los servicios:
```bash
docker-compose up --build
```

## Uso de la Aplicación

Una vez que los servicios estén corriendo, la aplicación estará disponible en:
- `http://localhost:5000`

### Endpoints disponibles:

#### 1. Registro de Usuario
- **POST `/auth/register`**
  - **Body**:
    ```json
    {
        "email": "usuario@empresa.com",
        "password": "contraseña_segura"
    }
    ```
  - **Respuesta**:
    ```json
    {
        "message": "Usuario registrado exitosamente"
    }
    ```

#### 2. Login
- **POST `/auth/login`**
  - **Body**:
    ```json
    {
        "email": "importador.activo@empresa.com",
        "password": "hash_de_prueba_123"
    }
    ```
  - **Respuesta**:
    ```json
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInT5cCI6IkpXVCJ9..."
    }
    ```

#### 3. Recurso Protegido
- **GET `/auth/protected`**
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
