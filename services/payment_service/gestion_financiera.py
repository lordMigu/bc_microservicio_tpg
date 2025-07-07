from flask import Blueprint, request
from services.utils import execute_sp, service_response
from loguru import logger

logger.add("gestion_financiera.log",
    rotation="1 day",
    retention="7 days",
)
from datetime import datetime

finanzas_bp = Blueprint('finanzas', __name__)

# API-TPG Servicio_Consulta_Estados_Cuenta
# Propósito: Consulta estados de cuenta (facturas, saldos pendientes)
@finanzas_bp.route('/estados_cuenta', methods=['GET'])
def consulta_estados_cuenta():
    # Defecto: los últimos 3 meses
    default_fecha_desde = datetime.now().replace(day=1, month=datetime.now().month-2).strftime('%Y-%m-%d')
    
    params = {
        'ruc_cliente': request.args.get('ruc_cliente'),
        'usuario': request.args.get('usuario'),
        'fecha_inicio': request.args.get('fecha_inicio', default_fecha_desde),
        'fecha_fin': request.args.get('fecha_fin', datetime.now().strftime('%Y-%m-%d'))
    }
    logger.info(f"Params: {params}")
    result, error = execute_sp('sp_consulta_estados_cuenta', params)
    logger.info(f"Result: {result}")
    logger.info(f"Error: {error}")
    return service_response(result, error)
