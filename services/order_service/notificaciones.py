from flask import Blueprint, request
from services.utils import service_response, execute_sp, require_params
from loguru import logger

logger.add("notificaciones.log",
    rotation="1 day",
    retention="7 days",
)
from loguru import logger

logger.add("app.log",
    rotation="1 day",
    retention="7 days",
)

# API-TPG Notificaciones_a_usuarios
# Documento de referencia: Opción Notificaciones
# prefijo /notificaciones 
notificaciones_bp = Blueprint('notifications_bp', __name__)

# En app.py
# -> app.register_blueprint(notifications_bp, url_prefix='/notifications')

# API-TPG Notificaciones_a_usuarios
@notificaciones_bp.route('/notificaciones', methods=['GET'])
def notificaciones():
    logger.info("Endpoint de notificaciones accedido")
    return service_response({"message": "Notificaciones a usuarios"})

@notificaciones_bp.route('/', methods=['GET'])
def get_notifications():
    """
    Este endpoint consulta y devuelve todas las notificaciones para el usuario autenticado.
    La integración se realiza mediante una llamada a la API "API-TPG Notificaciones_a_usuarios".
    """
    try:
        params = {
            'usuario': request.args.get('usuario'),
            'fecha_desde': request.args.get('fecha_desde', ''),
            'fecha_hasta': request.args.get('fecha_hasta', '')
        }
        logger.info(f"Params: {params}")
        result, error = execute_sp('sp_consulta_notificaciones', params, single_row=False)
        return service_response(result, error)

    except Exception as e:
        logger.error(f"Error inesperado en get_notifications: {str(e)}")
        # Devuelve código 3 para error interno
        return service_response(None, str(e), custom_code=3)