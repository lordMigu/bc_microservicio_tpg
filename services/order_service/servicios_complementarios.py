from flask import Blueprint, request
from services.utils import execute_sp, service_response
from loguru import logger

logger.add("servicios_complementarios.log",
    rotation="1 day",
    retention="7 days",
)

servicios_complementarios_bp = Blueprint('servicios_complementarios', __name__)

# API-TPG Servicio_Consulta_Complementarios_BL
# Propósito: Consulta servicios complementarios para un Bill of Lading (import)
@servicios_complementarios_bp.route('/complementarios_bl', methods=['GET'])
def consulta_complementarios_bl():
    params = {
        'numero_bl': request.args.get('numero_bl'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario'),
        'estado': request.args.get('estado', 'Todos'),  # Default: 'Todos'
        'fecha_desde': request.args.get('fecha_desde'),
        'fecha_hasta': request.args.get('fecha_hasta')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_complementarios_bl', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG Servicio_Consulta_Complementarios_Booking
# Propósito: Consulta servicios complementarios para un Booking (export)
@servicios_complementarios_bp.route('/complementarios_booking', methods=['GET'])
def consulta_complementarios_booking():
    params = {
        'numero_booking': request.args.get('numero_booking'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario'),
        'estado': request.args.get('estado', 'Todos'),  # Default: 'Todos'
        'fecha_desde': request.args.get('fecha_desde'),
        'fecha_hasta': request.args.get('fecha_hasta')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_complementarios_booking', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG Servicio_Consulta_Complementarios_Contenedor_Impo
# Propósito: Consulta servicios complementarios para un contenedor de importación
@servicios_complementarios_bp.route('/complementarios_contenedor_impo', methods=['GET'])
def consulta_complementarios_contenedor_impo():
    params = {
        'numero_contenedor': request.args.get('numero_contenedor'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_complementarios_contenedor_impo', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)

# API-TPG Servicio_Consulta_Complementarios_Contenedor_Expo
# Propósito: Consulta servicios complementarios para un contenedor de exportación
@servicios_complementarios_bp.route('/complementarios_contenedor_expo', methods=['GET'])
def consulta_complementarios_contenedor_expo():
    params = {
        'numero_contenedor': request.args.get('numero_contenedor'),
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario')
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_complementarios_contenedor_expo', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)