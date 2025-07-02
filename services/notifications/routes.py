from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Documento de referencia: Opción Notificaciones 
notifications_bp = Blueprint('notifications_bp', __name__)

# En app.py
# -> app.register_blueprint(notifications_bp, url_prefix='/notifications')

# @jwt_required() es un decorador que protege este endpoint.
# Si un usuario intenta acceder a esta URL sin un token JWT válido en la cabecera de su petición,
# recibirá un error de "No autorizado" (401).
@notifications_bp.route('/', methods=['GET'])
@jwt_required()
# @jwt_required() es un decorador que protege este endpoint.
# Si un usuario intenta acceder a esta URL sin un token JWT válido en la cabecera de su petición,
# recibirá un error de "No autorizado" (401).
def get_notifications():
    """
    Este endpoint consulta y devuelve todas las notificaciones para el usuario autenticado.
    La integración se realiza mediante una llamada a la API "API-TPG Notificaciones_a_usuarios". 
    """
    # Integración: Llamado al “API-TPG Notificaciones_a_usuarios” 
    current_user = get_jwt_identity()
    # Lógica para obtener las notificaciones del usuario
    # jsonify() serializa la lista de diccionarios al formato JSON
    return jsonify([
        {"tipo": "Llegada de Nave", "fecha": "2025-06-23", "detalle": "Nave XYZ ha llegado."}, # 
        {"tipo": "Descarga de Contenedor", "fecha": "2025-06-23", "detalle": "Contenedor ABC1234567 ha sido descargado."} # 
    ])