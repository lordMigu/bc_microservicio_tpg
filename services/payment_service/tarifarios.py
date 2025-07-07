from flask import Blueprint, request
from services.utils import execute_sp, service_response
from loguru import logger

logger.add("tarifarios.log",
    rotation="1 day",
    retention="7 days",
)

tarifarios_bp = Blueprint('tarifarios', __name__)

# API-TPG Servicio_Consulta_Tarifario_Repesaje_Contenedor
# Propósito: Consulta tarifario de repesaje de contenedor
@tarifarios_bp.route('/repesaje_contenedor', methods=['GET'])
def consulta_tarifario_repesaje():
    params = {
        'numero_contenedor': request.args.get('numero_contenedor'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    
    # Validación de parámetros
    if not all(params.values()):
        return service_response(None, 'Parámetros incompletos')
    
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_tarifario_repesaje', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    
    # Standardize response format
    if result.get('error'):
        return service_response(None, result['error'])
    return service_response(result, error)

# API-TPG Servicio_Consulta_Tarifario_Verificacion_Sello
# Propósito: Consulta tarifario de verificación de sello
@tarifarios_bp.route('/verificacion_sello', methods=['GET'])
def consulta_tarifario_verificacion_sello():
    params = {
        'numero_contenedor': request.args.get('numero_contenedor'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    
    # Validación de parámetros
    if not all(params.values()):
        return service_response(None, 'Parámetros incompletos')
    
    logger.info(f"Params: {params}")    
    result, error = execute_sp('sp_consulta_tarifario_verificacion_sello', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    
    # Standardize response format
    if result and result.get('error'):
        return service_response(None, result['error'])
    return service_response(result, error)


# API-TPG Servicio_Consulta_Tarifario_Repesaje_Carga_Suelta
# Purpose: Get loose cargo re-weighing tariff information
@tarifarios_bp.route('/repesaje_carga_suelta', methods=['GET'])
def consulta_tarifario_repesaje_carga_suelta():
    params = {
        'numero_bl': request.args.get('numero_bl'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    
    # Validate required parameters
    if not all(params.values()):
        return service_response(None, 'Parámetros incompletos')
    
    logger.info(f"Params: {params}")    
    result, error = execute_sp('sp_consulta_tarifario_repesaje_carga_suelta', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    
    # Standardize response format
    if result and result.get('error'):
        return service_response(None, result['error'])
        
    return service_response(result, error)

# API-TPG Servicio_Consulta_Tarifario_Despaletizar
# Propósito: Obtener información tarifaria para el servicio de despaletización
@tarifarios_bp.route('/tarifario_despaletizar', methods=['GET'])
def consulta_tarifario_despaletizar():
    parametros = {
        'numero_bl': request.args.get('numero_bl'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    
    # Validar parámetros obligatorios
    if not all(parametros.values()):
        return service_response(None, 'Parámetros incompletos')
    
    logger.info(f"Params: {parametros}")
    result, error = execute_sp('sp_consulta_tarifario_despaletizar', parametros)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    
    # Manejo de errores
    if result and result.get('error'):
        return service_response(None, result['error'])
        
    return service_response(result, error)