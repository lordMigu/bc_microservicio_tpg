from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

# Documento de referencia: Opción Servicios Complementarios Importador 
complementary_importer_bp = Blueprint('complementary_importer_bp', __name__)

@complementary_importer_bp.route('/by-bill-of-lading', methods=['GET'])
@jwt_required()
def get_services_by_bl():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Complementarios_BL” 
    bl_number = request.args.get('bl_number')
    return jsonify({"message": f"Servicios complementarios para el BL {bl_number}"})

@complementary_importer_bp.route('/by-container', methods=['GET'])
@jwt_required()
def get_services_by_container():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Complementarios_Contenedor_Impo” 
    container_number = request.args.get('container_number')
    return jsonify({"message": f"Servicios complementarios para el contenedor {container_number}"})

@complementary_importer_bp.route('/container-reweigh-tariff', methods=['GET'])
@jwt_required()
def get_container_reweigh_tariff():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Tarifario_Repesaje_Contenedor” 
    container_number = request.args.get('container_number')
    return jsonify({"message": f"Tarifa de repesaje para el contenedor {container_number}"})

@complementary_importer_bp.route('/request-container-reweigh', methods=['POST'])
@jwt_required()
def request_container_reweigh():
    # Integración: Llamado al “API-TPG Servicio_Solicitud_Repesaje_Contenedor” 
    data = request.get_json()
    return jsonify({"message": f"Solicitud de repesaje enviada para el contenedor {data.get('container_number')}"}), 202

@complementary_importer_bp.route('/seal-verification-tariff', methods=['GET'])
@jwt_required()
def get_seal_verification_tariff():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Tarifario_Verificacion_Sello” 
    container_number = request.args.get('container_number')
    return jsonify({"message": f"Tarifa de verificación de sello para el contenedor {container_number}"})

@complementary_importer_bp.route('/request-seal-verification', methods=['POST'])
@jwt_required()
def request_seal_verification():
    # Integración: Llamado al “API-TPG Servicio_Solicitud_Verificacion_Sello” 
    data = request.get_json()
    return jsonify({"message": f"Solicitud de verificación de sello enviada para el contenedor {data.get('container_number')}"}), 202

@complementary_importer_bp.route('/loose-cargo-reweigh-tariff', methods=['GET'])
@jwt_required()
def get_loose_cargo_reweigh_tariff():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Tarifario_Repesaje_Carga_Suelta” 
    bl_number = request.args.get('bl_number')
    return jsonify({"message": f"Tarifa de repesaje para carga suelta del BL {bl_number}"})

@complementary_importer_bp.route('/request-loose-cargo-reweigh', methods=['POST'])
@jwt_required()
def request_loose_cargo_reweigh():
    # Integración: Llamado al “API-TPG Servicio_Solicitud_Repesaje_Carga_Suelta” 
    data = request.get_json()
    return jsonify({"message": f"Solicitud de repesaje para carga suelta del BL {data.get('bl_number')} enviada"}), 202

@complementary_importer_bp.route('/depalletize-tariff', methods=['GET'])
@jwt_required()
def get_depalletize_tariff():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Tarifario_Despaletizar” 
    bl_number = request.args.get('bl_number')
    return jsonify({"message": f"Tarifa de despaletización para el BL {bl_number}"})

@complementary_importer_bp.route('/request-cargo-reassembly', methods=['POST'])
@jwt_required()
def request_cargo_reassembly():
    # Integración: Llamado al “API-TPG Servicio_Solicitud_Remontaje de Carga” 
    data = request.get_json()
    return jsonify({"message": "Solicitud de remontaje de carga enviada"}), 202

@complementary_importer_bp.route('/request-depalletization', methods=['POST'])
@jwt_required()
def request_depalletization():
    # Integración: Llamado al “API-TPG Servicio_Solicitud_Despaletizacion” 
    data = request.get_json()
    return jsonify({"message": "Solicitud de despaletización enviada"}), 202