-- Script para crear los procedimientos almacenados (MSSQL)
USE PruebaMicroServicios;
GO

-- Procedimientos Almacenados
CREATE OR ALTER PROCEDURE sp_consulta_info_booking
    @booking_id NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT * FROM Bookings WHERE booking_id = @booking_id AND ruc_cliente = @ruc_cliente;
END;
GO

CREATE OR ALTER PROCEDURE sp_consulta_contenedor_impo
    @numero_contenedor NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT peso, puerto, mrn, fecha_llegada, dress, eventos, aforos, almacenaje, despacho
    FROM Contenedores
    WHERE numero_contenedor = @numero_contenedor AND ruc_cliente = @ruc_cliente AND tipo_importacion = 1;
END;
GO

CREATE OR ALTER PROCEDURE sp_consulta_contenedor_expo
    @numero_contenedor NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT disv, dae, fecha_embarque, conexiones, estados, roleo
    FROM Contenedores
    WHERE numero_contenedor = @numero_contenedor AND ruc_cliente = @ruc_cliente AND tipo_importacion = 0;
END;
GO

CREATE OR ALTER PROCEDURE sp_consulta_info_bl
    @numero_bl NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT contenedor_desconsolidacion, tarja, bultos, peso, almacenaje, despacho
    FROM BLCargaSuelta
    WHERE numero_bl = @numero_bl AND ruc_cliente = @ruc_cliente;
END;
GO

-- Procedimientos Almacenados para Aforos, Inspecciones y Tarjas

CREATE OR ALTER PROCEDURE sp_consulta_programacion_aforo_bl
    @numero_bl NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT * FROM Aforos WHERE numero_bl = @numero_bl AND ruc_cliente = @ruc_cliente;
END;
GO

CREATE OR ALTER PROCEDURE sp_consulta_aforo_contenedor
    @numero_contenedor NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT * FROM Aforos WHERE numero_contenedor = @numero_contenedor AND ruc_cliente = @ruc_cliente;
END;
GO

CREATE OR ALTER PROCEDURE sp_consulta_requerimientos_contenedores_inspeccion
    @booking_id NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT * FROM Inspecciones WHERE booking_id = @booking_id AND ruc_cliente = @ruc_cliente;
END;
GO

CREATE OR ALTER PROCEDURE sp_consulta_inspeccion_contenedor_expo
    @numero_contenedor NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT * FROM Inspecciones WHERE numero_contenedor = @numero_contenedor AND ruc_cliente = @ruc_cliente;
END;
GO

CREATE OR ALTER PROCEDURE sp_consulta_tarja_carga_suelta
    @numero_bl NVARCHAR(50),
    @ruc_cliente NVARCHAR(20)
AS
BEGIN
    SELECT * FROM Tarjas WHERE numero_bl = @numero_bl AND ruc_cliente = @ruc_cliente;
END;
GO
