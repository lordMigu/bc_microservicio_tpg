from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

# Documento de referencia: Opción Trazabilidad Perfil Exportador 
traceability_exporter_bp = Blueprint('traceability_exporter_bp', __name__)

@traceability_exporter_bp.route('/booking-info', methods=['GET'])
@jwt_required()
def get_booking_info():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Info_Booking” 
    booking_number = request.args.get('booking_number')
    return jsonify({"message": f"Información del booking {booking_number}"})

@traceability_exporter_bp.route('/inspection-requirements', methods=['GET'])
@jwt_required()
def get_inspection_requirements():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Requerimientos_ContenedoresInspeccion” 
    booking_number = request.args.get('booking_number')
    return jsonify({"message": f"Requerimientos de inspección para el booking {booking_number}"})

@traceability_exporter_bp.route('/container', methods=['GET'])
@jwt_required()
def get_container_info():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Contenedor_Expo” 
    container_number = request.args.get('container_number')
    return jsonify({"message": f"Información del contenedor de exportación {container_number}"})

@traceability_exporter_bp.route('/container-inspection', methods=['GET'])
@jwt_required()
def get_container_inspection():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Inspeccion_Contenedor_Expo” 
    container_number = request.args.get('container_number')
    return jsonify({"message": f"Inspección del contenedor de exportación {container_number}"})