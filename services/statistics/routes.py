from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

# Documento de referencia: Opción Estadísticas e Indicadores 
statistics_bp = Blueprint('statistics_bp', __name__)

@statistics_bp.route('/import', methods=['GET'])
@jwt_required()
def get_import_statistics():
    # Esta sección describe los datos a mostrar, que se obtienen de varias fuentes 
    # La lógica para consultar Salesforce y otros sistemas TPG iría aquí. 
    return jsonify({
        "tiempo_promedio_despachos": "...", # 
        "contenedores_aforados_rayos_x": "...", # 
        "promedio_almacenaje": "...", # 
        "contenedores_descargados": "..."  # 
    })

@statistics_bp.route('/export', methods=['GET'])
@jwt_required()
def get_export_statistics():
    # Esta sección detalla las estadísticas de exportación a presentar.
    return jsonify({
        "contenedores_exportados_total": "...", # 
        "tiempo_permanencia_patio": "...", # 
        "unidades_ingresadas_antes_cutoff": "...", # 
        "tiempo_atencion_camiones": "..." # 
    })