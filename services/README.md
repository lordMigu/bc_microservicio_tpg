# Catálogo de Endpoints de Servicios

Esta tabla resume todos los endpoints expuestos por los blueprints registrados en `app.py`.  Cada ruta final (URL **completa**) ya incluye el prefijo de blueprint indicado en el registro.

| Módulo (Blueprint) | API-TPG | Método(s) | Endpoint | Propósito |
|--------------------|---------|-----------|----------|-----------|
|--------------------|-----------|-------------------|--------------------|
| notifications_bp | Notificaciones_a_usuarios | GET | `/notifications/` | Obtener notificaciones. |
| finanzas_bp | Servicio_Consulta_Estados_Cuenta | GET | `/finanzas/estados_cuenta` | Consultar estados de cuenta del cliente. |
| servicios_complementarios_bp | Servicio_Consulta_Complementarios_BL | GET | `/servicios_complementarios/complementarios_bl` | Consulta complementarios por BL. |
|  | Servicio_Consulta_Complementarios_Booking | GET | `/servicios_complementarios/complementarios_booking` | Complementarios por booking. |
|  | Servicio_Consulta_Complementarios_Contenedor_Impo | GET | `/servicios_complementarios/complementarios_contenedor_impo` | Complementarios contenedor importación. |
|  | Servicio_Consulta_Complementarios_Contenedor_Expo | GET | `/servicios_complementarios/complementarios_contenedor_expo` | Complementarios contenedor exportación. |
| consulta_info_bp | Servicio_Consulta_Info_BL | GET | `/consulta_info/info_bl` | Información general por BL. |
|  | Servicio_Consulta_Contenedor_Impo | GET | `/consulta_info/contenedor_impo` | Información contenedor importación. |
|  | Servicio_Consulta_Contenedor_Expo | GET | `/consulta_info/contenedor_expo` | Información contenedor exportación. |
|  | Servicio_Consulta_Info_Booking | GET | `/consulta_info/info_booking` | Información general por booking. |
| auxiliares_bp | Servicio_Consulta_Uso_App | GET | `/auxiliares/consulta_uso_app` | Registrar uso de la aplicación. |
|  | Servicio_Consulta_Tarja_Carga_Suelta | GET | `/auxiliares/consulta_tarja_carga_suelta` | Consulta tarja carga suelta. |
|  | Servicio_Consulta_Requerimientos_Contenedores_Inspeccion | GET | `/auxiliares/requerimientos_inspeccion` | Contenedores para inspección. |
|  | Servicio_Registro_Estadisticas_Importacion | POST | `/auxiliares/registro_estadisticas_impo` | Registrar estadísticas importación. |
|  | Servicio_Registro_Estadisticas_Exportacion | POST | `/auxiliares/registro_estadisticas_expo` | Registrar estadísticas exportación. |
|  | Servicio_Registro_Estadisticas_Importacion_Carga_Suelta | POST | `/auxiliares/registro_estadisticas_impo_carga_suelta` | Registrar estad. impo carga suelta. |
| tarifarios_bp | Servicio_Consulta_Tarifario_Repesaje_Contenedor | GET | `/tarifarios/repesaje_contenedor` | Tarifario repesaje contenedor. |
|  | Servicio_Consulta_Tarifario_Verificacion_Sello | GET | `/tarifarios/verificacion_sello` | Tarifario verificación sello. |
|  | Servicio_Consulta_Tarifario_Repesaje_Carga_Suelta | GET | `/tarifarios/repesaje_carga_suelta` | Tarifario repesaje carga suelta. |
|  | Servicio_Consulta_Tarifario_Despaletizar | GET | `/tarifarios/tarifario_despaletizar` | Tarifario despaletizar carga. |
| aforo_inspeccion_bp | Servicio_Consulta_Programacion_Aforo_BL | GET | `/aforo_inspeccion/programacion_aforo_bl` | Programación aforo BL. |
|  | Servicio_Consulta_Aforo_Contenedor | GET | `/aforo_inspeccion/aforo_contenedor` | Aforo por contenedor. |
|  | Servicio_Consulta_Inspeccion_Contenedor_Expo | GET | `/aforo_inspeccion/inspeccion_contenedor_expo` | Inspección contenedor export. |

> Nota: Mantenga este archivo actualizado cuando se añadan, modifiquen o eliminen rutas.
