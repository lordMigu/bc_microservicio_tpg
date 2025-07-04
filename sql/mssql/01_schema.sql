-- Script para inicializar el esquema de la base de datos (MSSQL)

-- Crear base de datos si no existe
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'PruebaMicroServicios')
BEGIN
    CREATE DATABASE PruebaMicroServicios;
END;
GO

USE PruebaMicroServicios;
GO

-- Crear tabla de Usuarios si no existe
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Usuarios]') AND type in (N'U'))
BEGIN
    CREATE TABLE Usuarios (
        UsuarioID INT PRIMARY KEY IDENTITY(1,1),
        Email NVARCHAR(100) UNIQUE NOT NULL,
        PasswordHash NVARCHAR(255) NOT NULL,
        RucCliente NVARCHAR(20),
        NombreCliente NVARCHAR(100),
        PerfilCliente NVARCHAR(50),
        EstadoCuenta NVARCHAR(50) DEFAULT 'Activa',
        FechaCreacion DATETIME DEFAULT GETDATE(),
        UltimoLogin DATETIME
    );
END;
GO

-- Modificar tabla de usuarios para añadir ruc_cliente
IF NOT EXISTS (SELECT * FROM sys.columns WHERE Name = N'ruc_cliente' AND Object_ID = Object_ID(N'usuarios'))
BEGIN
    ALTER TABLE usuarios ADD ruc_cliente NVARCHAR(20);
END;
GO

-- Crear tabla de Bookings
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Bookings]') AND type in (N'U'))
BEGIN
    CREATE TABLE Bookings (
        id INT PRIMARY KEY IDENTITY(1,1),
        booking_id NVARCHAR(50) NOT NULL UNIQUE,
        ruc_cliente NVARCHAR(20) NOT NULL,
        buque NVARCHAR(100),
        mrn NVARCHAR(50),
        puerto_destino NVARCHAR(100),
        tipo_carga NVARCHAR(50),
        contenedores NVARCHAR(MAX),
        estados NVARCHAR(100),
        dae NVARCHAR(50),
        inspecciones NVARCHAR(100)
    );
END;
GO

-- Crear tabla de Contenedores
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Contenedores]') AND type in (N'U'))
BEGIN
    CREATE TABLE Contenedores (
        id INT PRIMARY KEY IDENTITY(1,1),
        numero_contenedor NVARCHAR(50) NOT NULL UNIQUE,
        tipo_importacion BIT, -- 1 para Importación, 0 para Exportación
        ruc_cliente NVARCHAR(20) NOT NULL,
        peso DECIMAL(10, 2),
        puerto NVARCHAR(100),
        mrn NVARCHAR(50),
        fecha_llegada DATETIME,
        dress NVARCHAR(50),
        eventos NVARCHAR(MAX),
        aforos NVARCHAR(100),
        almacenaje NVARCHAR(100),
        despacho NVARCHAR(100),
        disv NVARCHAR(50),
        dae NVARCHAR(50),
        fecha_embarque DATETIME,
        conexiones NVARCHAR(100),
        estados NVARCHAR(100),
        roleo NVARCHAR(50)
    );
END;
GO

-- Crear tabla de BLCargaSuelta
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[BLCargaSuelta]') AND type in (N'U'))
BEGIN
    CREATE TABLE BLCargaSuelta (
        id INT PRIMARY KEY IDENTITY(1,1),
        numero_bl NVARCHAR(50) NOT NULL UNIQUE,
        ruc_cliente NVARCHAR(20) NOT NULL,
        contenedor_desconsolidacion NVARCHAR(50),
        tarja NVARCHAR(50),
        bultos INT,
        peso DECIMAL(10, 2),
        almacenaje NVARCHAR(100),
        despacho NVARCHAR(100)
    );
END;
GO

-- Crear tabla de Aforos
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Aforos]') AND type in (N'U'))
BEGIN
    CREATE TABLE Aforos (
        id INT PRIMARY KEY IDENTITY(1,1),
        numero_bl NVARCHAR(50),
        numero_contenedor NVARCHAR(50),
        ruc_cliente NVARCHAR(20) NOT NULL,
        fecha_programacion DATETIME,
        tipo_aforo NVARCHAR(100),
        estado NVARCHAR(50)
    );
END;
GO

-- Crear tabla de Inspecciones
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Inspecciones]') AND type in (N'U'))
BEGIN
    CREATE TABLE Inspecciones (
        id INT PRIMARY KEY IDENTITY(1,1),
        booking_id NVARCHAR(50),
        numero_contenedor NVARCHAR(50),
        ruc_cliente NVARCHAR(20) NOT NULL,
        requerimiento NVARCHAR(200),
        fecha_inspeccion DATETIME,
        estado NVARCHAR(50)
    );
END;
GO

-- Crear tabla de Tarjas (Carga Suelta)
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Tarjas]') AND type in (N'U'))
BEGIN
    CREATE TABLE Tarjas (
        id INT PRIMARY KEY IDENTITY(1,1),
        numero_bl NVARCHAR(50) NOT NULL,
        ruc_cliente NVARCHAR(20) NOT NULL,
        numero_tarja NVARCHAR(50) NOT NULL UNIQUE,
        bultos INT,
        peso DECIMAL(10, 2),
        descripcion NVARCHAR(200)
    );
END;
GO
