from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

# Documento de referencia: Opción Trazabilidad Perfil Importador 
traceability_importer_bp = Blueprint('traceability_importer_bp', __name__)

@traceability_importer_bp.route('/bill-of-lading-info', methods=['GET'])
@jwt_required()
def get_bl_info():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Info_BL” 
    bl_number = request.args.get('bl_number')
    # Lógica de consulta
    return jsonify({"message": f"Información para el BL {bl_number}"})

@traceability_importer_bp.route('/stowage-schedule-bl', methods=['GET'])
@jwt_required()
def get_stowage_schedule_bl():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Programacion_Aforo_BL” 
    bl_number = request.args.get('bl_number')
    # Lógica de consulta
    return jsonify({"message": f"Programación de aforo para el BL {bl_number}"})

@traceability_importer_bp.route('/container', methods=['GET'])
@jwt_required()
def get_container_info():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Contenedor_Impo” 
    container_number = request.args.get('container_number')
    # Lógica de consulta
    return jsonify({"message": f"Información del contenedor de importación {container_number}"})

@traceability_importer_bp.route('/container-stowage', methods=['GET'])
@jwt_required()
def get_container_stowage():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Aforo_Contenedor” 
    container_number = request.args.get('container_number')
    # Lógica de consulta
    return jsonify({"message": f"Aforo del contenedor {container_number}"})

@traceability_importer_bp.route('/bill-of-lading-child-info', methods=['GET'])
@jwt_required()
def get_bl_child_info():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Info_BL” 
    bl_number = request.args.get('bl_number')
    # Lógica de consulta para BL Hijo
    return jsonify({"message": f"Información para el BL hijo {bl_number}"})

@traceability_importer_bp.route('/loose-cargo-tally', methods=['GET'])
@jwt_required()
def get_loose_cargo_tally():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Tarja_Carga_Suelta” 
    bl_number = request.args.get('bl_number')
    # Lógica de consulta
    return jsonify({"message": f"Consulta de tarja para carga suelta del BL {bl_number}"})