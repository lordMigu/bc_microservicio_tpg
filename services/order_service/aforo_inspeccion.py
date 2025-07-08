from flask import Blueprint, request
from services.utils import execute_sp, service_response, require_params
from loguru import logger

logger.add("aforo_inspeccion.log",
    rotation="1 day",
    retention="7 days",
)

aforo_inspeccion_bp = Blueprint('aforo_inspeccion', __name__)

# API-TPG Servicio_Aforo_Inspeccion
# Propósito: Consultar aforos e inspecciones
@aforo_inspeccion_bp.route('/aforos_inspecciones', methods=['GET'])
@require_params('numero_contenedor', 'ruc_cliente', 'usuario')
def consulta_aforos_inspecciones():
    try:
        params = {
            'numero_contenedor': request.args.get('numero_contenedor'),
            'ruc_cliente': request.args.get('ruc_cliente'),
            'usuario': request.args.get('usuario')
        }
        logger.info(f"Params: {params}")
        result, error = execute_sp('sp_consulta_aforos_inspecciones', params, single_row=False)
        return service_response(result, error)
    except Exception as e:
        logger.error(f"Error inesperado en consulta_aforos_inspecciones: {str(e)}")
        return service_response(None, str(e), custom_code=3)

# API-TPG Servicio_Consulta_Programacion_Aforo_BL
# Purpose: Get scheduled survey information for a Bill of Lading
@aforo_inspeccion_bp.route('/programacion_aforo_bl', methods=['GET'])
@require_params('numero_bl', 'ruc_cliente', 'usuario')
def consulta_programacion_aforo_bl():
    try:
        params = {
            'numero_bl': request.args.get('numero_bl'),
            'ruc_cliente': request.args.get('ruc_cliente'),
            'usuario': request.args.get('usuario')
        }
        logger.info(f"Params: {params}")
        data, error = execute_sp('sp_consulta_programacion_aforo_bl', params, single_row=False)
        return service_response(data, error)
    except Exception as e:
        logger.error(f"Error inesperado en consulta_programacion_aforo_bl: {str(e)}")
        return service_response(None, str(e), custom_code=3)

# API-TPG Servicio_Consulta_Aforo_Contenedor
# Purpose: Get detailed survey information for a specific container
@aforo_inspeccion_bp.route('/aforo_contenedor', methods=['GET'])
@require_params('numero_contenedor', 'ruc_cliente', 'usuario')
def consulta_aforo_contenedor():
    try:
        params = {
            'numero_contenedor': request.args.get('numero_contenedor'),
            'ruc_cliente': request.args.get('ruc_cliente'),
            'usuario': request.args.get('usuario')
        }
        logger.info(f"Params: {params}")
        data, error = execute_sp('sp_consulta_aforo_contenedor', params, single_row=False)
        return service_response(data, error)
    except Exception as e:
        logger.error(f"Error inesperado en consulta_aforo_contenedor: {str(e)}")
        return service_response(None, str(e), custom_code=3)

# API-TPG Servicio_Consulta_Inspeccion_Contenedor_Expo
# Propósito: Get inspection details for an export container
@aforo_inspeccion_bp.route('/inspeccion_contenedor_expo', methods=['GET'])
def consulta_inspeccion_contenedor_expo():
    try:
        params = {
            'numero_contenedor': request.args.get('numero_contenedor'),
            'ruc_cliente': request.args.get('ruc_cliente'),
            'usuario': request.args.get('usuario')
        }
        logger.info(f"Params: {params}")
        data, error = execute_sp('sp_consulta_inspeccion_contenedor_expo', params, single_row=False)
        return service_response(data, error)
    except Exception as e:
        logger.error(f"Error inesperado en consulta_inspeccion_contenedor_expo: {str(e)}")
        return service_response(None, str(e), custom_code=3)