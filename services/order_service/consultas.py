from flask import Blueprint, request
from services.utils import execute_sp, service_response
from loguru import logger

logger.add("app.log", # Archivo de log
    rotation="1 day",      # Rota el archivo cada día
    retention="7 days", # Retiene los últimos 7 días
    )
consulta_info_bp = Blueprint('consulta_info', __name__)

# API-TPG Servicio_Consulta_Info_BL
# Propósito: Consultar información general por BL
@consulta_info_bp.route('/info_bl', methods=['GET'])
def consulta_info_bl():
    params = {
        # 'numero_bl': request.args.get('numero_bl'), #En produccion descomentar segun el orden de parametros en stored procedure
        # 'ruc_cliente': request.args.get('ruc_cliente'),
        # 'usuario': request.args.get('usuario'),
        'NumeroBL': request.args.get('numero_bl')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_info_bl', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG Servicio_Consulta_Contenedor_Impo
# Propósito: Consultar contenedor importación
@consulta_info_bp.route('/contenedor_impo', methods=['GET'])
def consulta_contenedor_impo():
    params = {
        'numero_contenedor': request.args.get('numero_contenedor'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_contenedor_impo', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG Servicio_Consulta_Contenedor_Expo
# Propósito: Consultar contenedor exportación
@consulta_info_bp.route('/contenedor_expo', methods=['GET'])
def consulta_contenedor_expo():
    params = {
        'numero_contenedor': request.args.get('numero_contenedor'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_contenedor_expo', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG Servicio_Consulta_Info_Booking
# Propósito: Consultar información general por booking
@consulta_info_bp.route('/info_booking', methods=['GET'])
def consulta_info_booking():
    params = {
        'numero_booking': request.args.get('numero_booking'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_info_booking', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)