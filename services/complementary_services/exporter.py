from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

# Documento de referencia: Opción Servicios Complementarios Exportación 
complementary_exporter_bp = Blueprint('complementary_exporter_bp', __name__)

@complementary_exporter_bp.route('/by-booking', methods=['GET'])
@jwt_required()
def get_services_by_booking():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Complementarios_Booking” 
    booking_number = request.args.get('booking_number')
    return jsonify({"message": f"Servicios complementarios para el booking {booking_number}"})

@complementary_exporter_bp.route('/by-container', methods=['GET'])
@jwt_required()
def get_services_by_container():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Complementarios_Contenedor_Expo” 
    container_number = request.args.get('container_number')
    return jsonify({"message": f"Servicios complementarios para el contenedor de exportación {container_number}"})