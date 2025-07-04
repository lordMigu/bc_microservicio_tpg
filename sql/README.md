# Scripts de Base de Datos

Este directorio contiene los scripts SQL necesarios para inicializar y configurar la base de datos de la aplicación. Los scripts están organizados en subdirectorios según el motor de base de datos.

## Estructura

Cada subdirectorio de motor de base de datos (ej. `mssql`, `sybase`) contiene los siguientes scripts, que deben ejecutarse en orden:

1.  **`01_schema.sql`**: Este script crea la estructura de la base de datos, incluyendo tablas, vistas y relaciones.
2.  **`02_data.sql`**: Este script inserta los datos iniciales necesarios para el funcionamiento de la aplicación, como catálogos, usuarios por defecto, etc.
3.  **`03_procedures.sql`**: Este script crea los procedimientos almacenados que utiliza la aplicación para interactuar con la base de datos.

## Uso

Para inicializar la base de datos, ejecute los scripts en el orden numérico indicado dentro del directorio correspondiente a su motor de base de datos.
