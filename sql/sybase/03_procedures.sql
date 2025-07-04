-- Script para crear los procedimientos almacenados (Sybase)
use PruebaMicroServicios
go

print 'Creando procedimientos almacenados...'
go

if exists (select * from sysobjects where name = 'sp_consulta_info_booking' and type = 'P')
    drop procedure sp_consulta_info_booking
go
create procedure sp_consulta_info_booking
    @booking_id varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select * from Bookings where booking_id = @booking_id and ruc_cliente = @ruc_cliente
end
go

if exists (select * from sysobjects where name = 'sp_consulta_contenedor_impo' and type = 'P')
    drop procedure sp_consulta_contenedor_impo
go
create procedure sp_consulta_contenedor_impo
    @numero_contenedor varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select peso, puerto, mrn, fecha_llegada, dress, eventos, aforos, almacenaje, despacho
    from Contenedores
    where numero_contenedor = @numero_contenedor and ruc_cliente = @ruc_cliente and tipo_importacion = 1
end
go

if exists (select * from sysobjects where name = 'sp_consulta_contenedor_expo' and type = 'P')
    drop procedure sp_consulta_contenedor_expo
go
create procedure sp_consulta_contenedor_expo
    @numero_contenedor varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select disv, dae, fecha_embarque, conexiones, estados, roleo
    from Contenedores
    where numero_contenedor = @numero_contenedor and ruc_cliente = @ruc_cliente and tipo_importacion = 0
end
go

if exists (select * from sysobjects where name = 'sp_consulta_info_bl' and type = 'P')
    drop procedure sp_consulta_info_bl
go
create procedure sp_consulta_info_bl
    @numero_bl varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select contenedor_desconsolidacion, tarja, bultos, peso, almacenaje, despacho
    from BLCargaSuelta
    where numero_bl = @numero_bl and ruc_cliente = @ruc_cliente
end
go

if exists (select * from sysobjects where name = 'sp_consulta_programacion_aforo_bl' and type = 'P')
    drop procedure sp_consulta_programacion_aforo_bl
go
create procedure sp_consulta_programacion_aforo_bl
    @numero_bl varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select * from Aforos where numero_bl = @numero_bl and ruc_cliente = @ruc_cliente
end
go

if exists (select * from sysobjects where name = 'sp_consulta_aforo_contenedor' and type = 'P')
    drop procedure sp_consulta_aforo_contenedor
go
create procedure sp_consulta_aforo_contenedor
    @numero_contenedor varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select * from Aforos where numero_contenedor = @numero_contenedor and ruc_cliente = @ruc_cliente
end
go

if exists (select * from sysobjects where name = 'sp_consulta_requerimientos_contenedores_inspeccion' and type = 'P')
    drop procedure sp_consulta_requerimientos_contenedores_inspeccion
go
create procedure sp_consulta_requerimientos_contenedores_inspeccion
    @booking_id varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select * from Inspecciones where booking_id = @booking_id and ruc_cliente = @ruc_cliente
end
go

if exists (select * from sysobjects where name = 'sp_consulta_inspeccion_contenedor_expo' and type = 'P')
    drop procedure sp_consulta_inspeccion_contenedor_expo
go
create procedure sp_consulta_inspeccion_contenedor_expo
    @numero_contenedor varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select * from Inspecciones where numero_contenedor = @numero_contenedor and ruc_cliente = @ruc_cliente
end
go

if exists (select * from sysobjects where name = 'sp_consulta_tarja_carga_suelta' and type = 'P')
    drop procedure sp_consulta_tarja_carga_suelta
go
create procedure sp_consulta_tarja_carga_suelta
    @numero_bl varchar(50),
    @ruc_cliente varchar(20)
as
begin
    select * from Tarjas where numero_bl = @numero_bl and ruc_cliente = @ruc_cliente
end
go

print '--- Script de Sybase completado ---'
go
