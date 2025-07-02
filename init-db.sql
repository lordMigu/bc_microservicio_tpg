-- Script para inicializar la base de datos

-- Crear base de datos si no existe
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'PruebaMicroServicios')
BEGIN
    CREATE DATABASE PruebaMicroServicios;
END;
GO

USE PruebaMicroServicios;
GO

-- Crear tabla de usuarios
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[usuarios]') AND type in (N'U'))
BEGIN
    CREATE TABLE usuarios (
        id INT PRIMARY KEY IDENTITY(1,1),
        username NVARCHAR(50) NOT NULL UNIQUE,
        password_hash NVARCHAR(256) NOT NULL,
        email NVARCHAR(100) NOT NULL UNIQUE,
        nombre NVARCHAR(100),
        apellido NVARCHAR(100),
        fecha_registro DATETIME DEFAULT GETDATE(),
        estado BIT DEFAULT 1
    );
END;
GO

-- Crear tabla de roles
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[roles]') AND type in (N'U'))
BEGIN
    CREATE TABLE roles (
        id INT PRIMARY KEY IDENTITY(1,1),
        nombre NVARCHAR(50) NOT NULL UNIQUE,
        descripcion NVARCHAR(200)
    );
END;
GO

-- Crear tabla de usuarios_roles
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[usuarios_roles]') AND type in (N'U'))
BEGIN
    CREATE TABLE usuarios_roles (
        usuario_id INT,
        rol_id INT,
        PRIMARY KEY (usuario_id, rol_id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (rol_id) REFERENCES roles(id)
    );
END;
GO

-- Insertar roles básicos
IF NOT EXISTS (SELECT 1 FROM roles WHERE nombre = 'admin')
BEGIN
    INSERT INTO roles (nombre, descripcion) VALUES ('admin', 'Administrador del sistema');
END;

IF NOT EXISTS (SELECT 1 FROM roles WHERE nombre = 'usuario')
BEGIN
    INSERT INTO roles (nombre, descripcion) VALUES ('usuario', 'Usuario normal del sistema');
END;
GO

-- Crear usuario administrador por defecto
IF NOT EXISTS (SELECT 1 FROM usuarios WHERE username = 'admin')
BEGIN
    INSERT INTO usuarios (username, password_hash, email, nombre, apellido, estado)
    VALUES (
        'admin',
        'TU_HASH_PASSWORD_AQUI',  -- Deberías reemplazar esto con un hash real
        'admin@ejemplo.com',
        'Administrador',
        'Sistema',
        1
    );

    -- Asignar rol admin
    INSERT INTO usuarios_roles (usuario_id, rol_id)
    SELECT u.id, r.id
    FROM usuarios u, roles r
    WHERE u.username = 'admin' AND r.nombre = 'admin';
END;
GO
