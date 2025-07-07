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

-- Crear tabla de Bookings
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Bookings]') AND type in (N'U'))
BEGIN
    CREATE TABLE Bookings (
        numero_bl NVARCHAR(50) PRIMARY KEY,
        buque NVARCHAR(100),
        puerto_origen NVARCHAR(100),
        fecha_eta DATETIME2(0), -- Formato: YYYY-MM-DD HH:MM:SS
        fecha_descarga DATETIME2(0), -- Formato: YYYY-MM-DD HH:MM:SS
        mrn NVARCHAR(50),
        puerto_destino NVARCHAR(100),
        tipo_carga NVARCHAR(50),
        tipo_contenedor NVARCHAR(50),
        ruc_cliente NVARCHAR(20) NOT NULL,
        total_contenedores INT,
        total_contenedores_20 INT,
        total_contenedores_40 INT,
        unidades_facturadas INT,
        cont_programados_aforo INT,
        numero_contenedor NVARCHAR(50),
        tipo_contenedor NVARCHAR(50),
        fecha_confirmacion_ecuapass DATETIME2(0), -- Formato: YYYY-MM-DD HH:MM:SS
        numero_dress NVARCHAR(50),
        fecha_salida DATETIME2(0), -- Formato: YYYY-MM-DD HH:MM:SS
        tamaño_contenedor INT,
        programacion_aforo_fisica BIT, -- 1 para Sí, 0 para No
        programacion_rayos_x BIT, -- 1 para Sí, 0 para No
        contenedor_facturado BIT -- 1 para Sí, 0 para No
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
