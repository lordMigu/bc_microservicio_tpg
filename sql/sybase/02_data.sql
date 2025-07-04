-- Script para poblar la base de datos con datos de prueba (Sybase)
use PruebaMicroServicios
go

-- Insertar usuario de prueba si no existe
if not exists (select 1 from Usuarios where Email = 'test@example.com')
begin
    print 'Insertando usuario de prueba...'
    insert into Usuarios (Email, PasswordHash, RucCliente, NombreCliente, PerfilCliente, EstadoCuenta)
    values ('test@example.com', 'password123', '12345678901', 'Cliente de Prueba', 'Admin', 'Activa')
end
go

-- Insertar datos de prueba para Bookings, Contenedores, BLCargaSuelta
print 'Insertando datos de prueba en Bookings, Contenedores, BLCargaSuelta...'
go
insert into Bookings (booking_id, ruc_cliente, buque, mrn, puerto_destino, tipo_carga, contenedores, estados, dae, inspecciones) values ('BK-001', '12345678901', 'Buque Ejemplo', 'MRN-123', 'Puerto Destino A', 'Carga General', 'CONT1, CONT2', 'Activo', 'DAE-001', 'Ninguna')
go
insert into Contenedores (numero_contenedor, tipo_importacion, ruc_cliente, peso, puerto, mrn, fecha_llegada, dress, eventos, aforos, almacenaje, despacho) values ('CONT-IMPO-001', 1, '12345678901', 1500.50, 'Puerto Origen B', 'MRN-456', getdate(), 'DRESS-01', 'Llegada, Descarga', 'Aforo Físico', 'Bodega 5', 'Despachado')
go
insert into Contenedores (numero_contenedor, tipo_importacion, ruc_cliente, disv, dae, fecha_embarque, conexiones, estados, roleo) values ('CONT-EXPO-001', 0, '12345678901', 'DISV-02', 'DAE-002', getdate(), 'Conexión Eléctrica', 'Listo para embarque', 'No')
go
insert into BLCargaSuelta (numero_bl, ruc_cliente, contenedor_desconsolidacion, tarja, bultos, peso, almacenaje, despacho) values ('BL-CS-001', '12345678901', 'CONT-DESC-01', 'TARJA-123', 50, 500.75, 'Patio 3', 'En proceso')
go

-- Insertar datos de prueba para Aforos, Inspecciones y Tarjas
print 'Insertando datos de prueba en Aforos, Inspecciones, Tarjas...'
go
insert into Aforos (numero_bl, numero_contenedor, ruc_cliente, fecha_programacion, tipo_aforo, estado) values ('BL-CS-001', NULL, '12345678901', getdate(), 'Aforo Físico', 'Programado')
go
insert into Aforos (numero_bl, numero_contenedor, ruc_cliente, fecha_programacion, tipo_aforo, estado) values (NULL, 'CONT-IMPO-001', '12345678901', getdate(), 'Aforo Automático', 'Completado')
go
insert into Inspecciones (booking_id, numero_contenedor, ruc_cliente, requerimiento, fecha_inspeccion, estado) values ('BK-001', NULL, '12345678901', 'Inspección de Antinarcóticos', getdate(), 'Solicitado')
go
insert into Inspecciones (booking_id, numero_contenedor, ruc_cliente, requerimiento, fecha_inspeccion, estado) values (NULL, 'CONT-EXPO-001', '12345678901', 'Inspección de Rayos X', getdate(), 'Realizada')
go
insert into Tarjas (numero_bl, ruc_cliente, numero_tarja, bultos, peso, descripcion) values ('BL-CS-001', '12345678901', 'TARJA-CS-001', 10, 100.5, 'Cajas de repuestos')
go
