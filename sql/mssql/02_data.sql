-- Script para poblar la base de datos con datos de prueba (MSSQL)
USE PruebaMicroServicios;
GO

-- Insertar usuario de prueba si no existe
IF NOT EXISTS (SELECT 1 FROM Usuarios WHERE Email = 'test@example.com')
BEGIN
    INSERT INTO Usuarios (Email, PasswordHash, RucCliente, NombreCliente, PerfilCliente, EstadoCuenta)
    VALUES ('test@example.com', 'password123', '12345678901', 'Cliente de Prueba', 'Admin', 'Activa');
END;
GO

-- Insertar datos de prueba
-- (Asegúrate de que los RUC coincidan con los usuarios de prueba)
INSERT INTO Bookings (booking_id, ruc_cliente, buque, mrn, puerto_destino, tipo_carga, contenedores, estados, dae, inspecciones)
VALUES ('BK-001', '12345678901', 'Buque Ejemplo', 'MRN-123', 'Puerto Destino A', 'Carga General', 'CONT1, CONT2', 'Activo', 'DAE-001', 'Ninguna');

INSERT INTO Contenedores (numero_contenedor, tipo_importacion, ruc_cliente, peso, puerto, mrn, fecha_llegada, dress, eventos, aforos, almacenaje, despacho)
VALUES ('CONT-IMPO-001', 1, '12345678901', 1500.50, 'Puerto Origen B', 'MRN-456', GETDATE(), 'DRESS-01', 'Llegada, Descarga', 'Aforo Físico', 'Bodega 5', 'Despachado');

INSERT INTO Contenedores (numero_contenedor, tipo_importacion, ruc_cliente, disv, dae, fecha_embarque, conexiones, estados, roleo)
VALUES ('CONT-EXPO-001', 0, '12345678901', 'DISV-02', 'DAE-002', GETDATE(), 'Conexión Eléctrica', 'Listo para embarque', 'No');

INSERT INTO BLCargaSuelta (numero_bl, ruc_cliente, contenedor_desconsolidacion, tarja, bultos, peso, almacenaje, despacho)
VALUES ('BL-CS-001', '12345678901', 'CONT-DESC-01', 'TARJA-123', 50, 500.75, 'Patio 3', 'En proceso');
GO

-- Insertar datos de prueba para Aforos, Inspecciones y Tarjas
INSERT INTO Aforos (numero_bl, numero_contenedor, ruc_cliente, fecha_programacion, tipo_aforo, estado)
VALUES ('BL-CS-001', NULL, '12345678901', GETDATE(), 'Aforo Físico', 'Programado');

INSERT INTO Aforos (numero_bl, numero_contenedor, ruc_cliente, fecha_programacion, tipo_aforo, estado)
VALUES (NULL, 'CONT-IMPO-001', '12345678901', GETDATE(), 'Aforo Automático', 'Completado');

INSERT INTO Inspecciones (booking_id, numero_contenedor, ruc_cliente, requerimiento, fecha_inspeccion, estado)
VALUES ('BK-001', NULL, '12345678901', 'Inspección de Antinarcóticos', GETDATE(), 'Solicitado');

INSERT INTO Inspecciones (booking_id, numero_contenedor, ruc_cliente, requerimiento, fecha_inspeccion, estado)
VALUES (NULL, 'CONT-EXPO-001', '12345678901', 'Inspección de Rayos X', GETDATE(), 'Realizada');

INSERT INTO Tarjas (numero_bl, ruc_cliente, numero_tarja, bultos, peso, descripcion)
VALUES ('BL-CS-001', '12345678901', 'TARJA-CS-001', 10, 100.5, 'Cajas de repuestos');
GO
