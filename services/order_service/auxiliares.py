from flask import Blueprint, request
from services.utils import execute_sp, service_response
from loguru import logger

logger.add("app.log",
    rotation="1 day",
    retention="7 days",
)

auxiliares_bp = Blueprint('auxiliares', __name__)

# API-TPG: Servicio_Consulta_Uso_App
# Propósito: Registra trámites en la app para facturación posterior
@auxiliares_bp.route('/consulta_uso_app', methods=['GET'])
def consulta_uso_app():
    params = {
        'ruc_cliente': request.args.get('ruc_cliente'),
        'mrn': request.args.get('mrn'),
        'numero_contenedor': request.args.get('numero_contenedor', None),  # Opcional
        'numero_bl_hijo': request.args.get('numero_bl_hijo', None)        # Opcional
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_uso_app', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG: Servicio_Consulta_Tarja_Carga_Suelta
# Propósito: Consulta detalles de tarjas físicas para carga suelta
@auxiliares_bp.route('/consulta_tarja_carga_suelta', methods=['GET'])
def consulta_tarja_carga_suelta():
    params = {
        'numero_bl': request.args.get('numero_bl'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_tarja_carga_suelta', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG: Servicio_Consulta_Requerimientos_Contenedores_Inspeccion
# Propósito: Lista contenedores seleccionados para inspección en exportación
@auxiliares_bp.route('/requerimientos_inspeccion', methods=['GET'])
def requerimientos_inspeccion():
    params = {
        'numero_booking': request.args.get('numero_booking'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_requerimientos_inspeccion', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG: Servicio_Registro_Estadisticas_Importacion
# Propósito: Registra datos operativos para análisis (híbrido operativo/financiero)
@auxiliares_bp.route('/registro_estadisticas_impo', methods=['POST'])
def registro_estadisticas_impo():
    data = request.json
    logger.info(f"Params: {data}")
    result, error = execute_sp('sp_registro_estadisticas_impo', data)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG: Servicio_Registro_Estadisticas_Exportacion
# Propósito: Registra datos operativos para análisis (híbrido operativo/financiero)
@auxiliares_bp.route('/registro_estadisticas_expo', methods=['POST'])
def registro_estadisticas_expo():
    data = request.json
    logger.info(f"Params: {data}")
    result, error = execute_sp('sp_registro_estadisticas_expo', data)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG Servicio_Registro_Estadisticas_Importacion_Carga_Suelta
# Propósito: Registrar estadísticas operativas para carga suelta de importación
@auxiliares_bp.route('/registro_estadisticas_impo_carga_suelta', methods=['POST'])
def registro_estadisticas_impo_carga_suelta():
    campos_requeridos = [
        'numero_bl',
        'numero_tarja',
        'peso_manifestado',
        'peso_dress',
        'fecha_descarga',
        'fecha_despacho',
        'consolidadora'
    ] # Campos obligatorios
    
    datos = request.json # Datos recibidos
    
    # Validar campos obligatorios
    if not all(campo in datos for campo in campos_requeridos):
        return service_response(None, 'Campos obligatorios faltantes') 
    
    try:
        logger.info(f"Params: {datos}")
        result, error = execute_sp('sp_registro_estadisticas_impo_carga_suelta', datos)
        logger.info(f"Result: {result}")
        logger.info(f"Error: {error}")
        
        if result and result.get('error'):
            return service_response(None, result['error'])
                
        return service_response({
            'data': {
                'id_registro': result['data']['id'] if result and 'data' in result and 'id' in result['data'] else None,
                'resumen': {
                    'numero_tarja': datos.get('numero_tarja'),
                }
            },
            'error': None
        })
        
    except Exception as e:
        return service_response(None, f'Error en el procesamiento: {str(e)}')