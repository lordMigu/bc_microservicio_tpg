-- ======================================================
-- SCRIPT DE INICIALIZACIÓN DE ESQUEMA PARA SYBASE
-- ======================================================
go

-- Crear base de datos si no existe
if not exists (select * from master.dbo.sysdatabases where name = 'PruebaMicroServicios')
begin
    print 'Creando base de datos PruebaMicroServicios...'
    create database PruebaMicroServicios
end
go

use PruebaMicroServicios
go

-- Crear tabla de Usuarios si no existe
if not exists (select * from sysobjects where name = 'Usuarios' and type = 'U')
begin
    print 'Creando tabla Usuarios...'
    create table Usuarios (
        UsuarioID int identity primary key,
        Email varchar(100) unique not null,
        PasswordHash varchar(255) not null,
        RucCliente varchar(20) null,
        NombreCliente varchar(100) null,
        PerfilCliente varchar(50) null,
        EstadoCuenta varchar(50) default 'Activa',
        FechaCreacion datetime default getdate(),
        UltimoLogin datetime null
    )
end
go

-- Modificar tabla de usuarios para añadir ruc_cliente
if not exists (select * from syscolumns where id = object_id('Usuarios') and name = 'ruc_cliente')
begin
    print 'Añadiendo columna ruc_cliente a Usuarios...'
    alter table Usuarios add ruc_cliente varchar(20) null
end
go

-- Crear tabla de Bookings
if not exists (select * from sysobjects where name = 'Bookings' and type = 'U')
begin
    print 'Creando tabla Bookings...'
    create table Bookings (
        id int identity primary key,
        booking_id varchar(50) not null unique,
        ruc_cliente varchar(20) not null,
        buque varchar(100) null,
        mrn varchar(50) null,
        puerto_destino varchar(100) null,
        tipo_carga varchar(50) null,
        contenedores text null,
        estados varchar(100) null,
        dae varchar(50) null,
        inspecciones varchar(100) null
    )
end
go

-- Crear tabla de Contenedores
if not exists (select * from sysobjects where name = 'Contenedores' and type = 'U')
begin
    print 'Creando tabla Contenedores...'
    create table Contenedores (
        id int identity primary key,
        numero_contenedor varchar(50) not null unique,
        tipo_importacion tinyint,
        ruc_cliente varchar(20) not null,
        peso decimal(10, 2) null,
        puerto varchar(100) null,
        mrn varchar(50) null,
        fecha_llegada datetime null,
        dress varchar(50) null,
        eventos text null,
        aforos varchar(100) null,
        almacenaje varchar(100) null,
        despacho varchar(100) null,
        disv varchar(50) null,
        dae varchar(50) null,
        fecha_embarque datetime null,
        conexiones varchar(100) null,
        estados varchar(100) null,
        roleo varchar(50) null
    )
end
go

-- Crear tabla de BLCargaSuelta
if not exists (select * from sysobjects where name = 'BLCargaSuelta' and type = 'U')
begin
    print 'Creando tabla BLCargaSuelta...'
    create table BLCargaSuelta (
        id int identity primary key,
        numero_bl varchar(50) not null unique,
        ruc_cliente varchar(20) not null,
        contenedor_desconsolidacion varchar(50) null,
        tarja varchar(50) null,
        bultos int null,
        peso decimal(10, 2) null,
        almacenaje varchar(100) null,
        despacho varchar(100) null
    )
end
go

-- Crear tabla de Aforos
if not exists (select * from sysobjects where name = 'Aforos' and type = 'U')
begin
    print 'Creando tabla Aforos...'
    create table Aforos (
        id int identity primary key,
        numero_bl varchar(50) null,
        numero_contenedor varchar(50) null,
        ruc_cliente varchar(20) not null,
        fecha_programacion datetime null,
        tipo_aforo varchar(100) null,
        estado varchar(50) null
    )
end
go

-- Crear tabla de Inspecciones
if not exists (select * from sysobjects where name = 'Inspecciones' and type = 'U')
begin
    print 'Creando tabla Inspecciones...'
    create table Inspecciones (
        id int identity primary key,
        booking_id varchar(50) null,
        numero_contenedor varchar(50) null,
        ruc_cliente varchar(20) not null,
        requerimiento varchar(200) null,
        fecha_inspeccion datetime null,
        estado varchar(50) null
    )
end
go

-- Crear tabla de Tarjas (Carga Suelta)
if not exists (select * from sysobjects where name = 'Tarjas' and type = 'U')
begin
    print 'Creando tabla Tarjas...'
    create table Tarjas (
        id int identity primary key,
        numero_bl varchar(50) not null,
        ruc_cliente varchar(20) not null,
        numero_tarja varchar(50) not null unique,
        bultos int null,
        peso decimal(10, 2) null,
        descripcion varchar(200) null
    )
end
go
