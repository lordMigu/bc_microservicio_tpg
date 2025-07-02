from flask import Blueprint, jsonify, request, redirect
from flask_jwt_extended import jwt_required

# Documento de referencia: Opción Gestión Financiera 
financial_bp = Blueprint('financial_bp', __name__)

@financial_bp.route('/presettlement/import-container', methods=['GET'])
@jwt_required()
def presettlement_import_container():
    # Redirecciona a la página de Cálculo TPG en DISV. 
    return redirect("https://www.tpg.com.ec/webtpg/index.php")

@financial_bp.route('/presettlement/import-loose-cargo', methods=['GET'])
@jwt_required()
def presettlement_import_loose_cargo():
    # Redirecciona a la página de Cálculo TPG en DISV. 
    return redirect("https://www.tpg.com.ec/webtpg/index.php")

@financial_bp.route('/presettlement/export-container', methods=['GET'])
@jwt_required()
def presettlement_export_container():
    # Redirecciona a la página Proformas Exportación en DISV (Login). 
    return redirect("https://www.tpg.com.ec/webtpg/index.php")

@financial_bp.route('/account-statements', methods=['GET'])
@jwt_required()
def get_account_statements():
    # Integración: Llamado al “API-TPG Servicio_Consulta_Estados_Cuenta” 
    # Lógica para consultar el detalle de facturas
    return jsonify({
        "cantidad_facturas_generadas": 10,
        "cantidad_facturas_pendiente_pago": 2,
        "monto_total_pendiente": "5000.00 USD"
    })