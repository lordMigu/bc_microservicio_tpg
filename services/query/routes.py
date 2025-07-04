from flask import Blueprint, jsonify, request

from database.database import get_db

query_bp = Blueprint('query_bp', __name__)

def execute_sp(sp_name, params, single_row=True):
    """
    Ejecuta un procedimiento almacenado y devuelve los resultados.
    """
    try:
        with get_db() as conn:
            with conn.cursor() as cursor:
                placeholders = ', '.join(['?'] * len(params))
                cursor.execute(f"EXEC {sp_name} {placeholders}", params)
                
                columns = [column[0] for column in cursor.description]
                
                if single_row:
                    row = cursor.fetchone()
                    if row:
                        return dict(zip(columns, row)), None
                    return None, "No se encontraron datos."
                else:
                    rows = cursor.fetchall()
                    if rows:
                        return [dict(zip(columns, row)) for row in rows], None
                    return [], "No se encontraron datos."
    except Exception as e:
        return None, str(e)

@query_bp.route('/booking', methods=['GET'])
def get_booking_info():
    """
    1. Consulta de número de Booking
    """
    booking_id = request.args.get('booking_id')
    ruc_cliente = request.args.get('ruc_cliente')
    
    if not booking_id or not ruc_cliente:
        return jsonify({"error": "Faltan parámetros requeridos: booking_id, ruc_cliente"}), 400

    data, error = execute_sp('sp_consulta_info_booking', (booking_id, ruc_cliente))
    
    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)

@query_bp.route('/container/import', methods=['GET'])
def get_container_import_info():
    """
    2. Consulta de contenedor Importación
    
    Esta consulta devuelve todos los contenedores de importación que coinciden con los parámetros de
    búsqueda: ruc_cliente, fecha_inicio y fecha_fin.
    
    Parámetros:
    - numero_contenedor: El número del contenedor que se desea buscar.
    - ruc_cliente: El RUC del cliente que realizó el booking.
    """
    numero_contenedor = request.args.get('numero_contenedor')
    ruc_cliente = request.args.get('ruc_cliente')
    
    # Si no se proporcionan todos los parámetros, se retorna un error con codigo 400 que indica que faltan parámetros requeridos
    if not all([numero_contenedor, ruc_cliente]):
        return jsonify({"error": "Faltan parámetros requeridos: numero_contenedor, ruc_cliente"}), 400

    # Se ejecuta el procedimiento almacenado sp_consulta_contenedor_impo con los parámetros proporcionados
    # single_row=False indica que se espera una lista de resultados
    data, error = execute_sp('sp_consulta_contenedor_impo', (numero_contenedor, ruc_cliente), single_row=False)

    # Si ocurre un error, se retorna un error con codigo 404 si el error indica que no se encontraron datos,
    # de lo contrario se retorna un error con codigo 500
    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)

@query_bp.route('/container/export', methods=['GET'])
def get_container_export_info():
    """
    3. Consulta de contenedor Exportación
    """
    ruc_cliente = request.args.get('ruc_cliente')
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')

    # Si no se proporcionan todos los parámetros, se retorna un error con codigo 400 que indica que faltan parámetros requeridos
    if not all([ruc_cliente, fecha_inicio, fecha_fin]):
        return jsonify({"error": "Faltan parámetros requeridos: ruc_cliente, fecha_inicio, fecha_fin"}), 400

    data, error = execute_sp('sp_consulta_contenedores_exportacion', (ruc_cliente, fecha_inicio, fecha_fin), single_row=False)

    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)

@query_bp.route('/bl-loose-cargo', methods=['GET'])
def get_bl_info():
    """
    4. Consulta de BL de carga suelta (BL hijo)
    """
    numero_bl = request.args.get('numero_bl')
    ruc_cliente = request.args.get('ruc_cliente')

    if not numero_bl or not ruc_cliente:
        return jsonify({"error": "Faltan parámetros requeridos: numero_bl, ruc_cliente"}), 400

    data, error = execute_sp('sp_consulta_info_bl', (numero_bl, ruc_cliente))

    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)

@query_bp.route('/aforo/bl', methods=['GET'])
def get_aforo_bl_info():
    """
    5.a. Consulta de Aforo por BL
    """
    numero_bl = request.args.get('numero_bl')
    ruc_cliente = request.args.get('ruc_cliente')

    if not numero_bl or not ruc_cliente:
        return jsonify({"error": "Faltan parámetros requeridos: numero_bl, ruc_cliente"}), 400

    data, error = execute_sp('sp_consulta_programacion_aforo_bl', (numero_bl, ruc_cliente), single_row=False)

    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)

@query_bp.route('/aforo/container', methods=['GET'])
def get_aforo_container_info():
    """
    5.b. Consulta de Aforo por Contenedor
    """
    contenedor_id = request.args.get('contenedor_id')
    ruc_cliente = request.args.get('ruc_cliente')

    if not contenedor_id or not ruc_cliente:
        return jsonify({"error": "Faltan parámetros requeridos: contenedor_id, ruc_cliente"}), 400

    data, error = execute_sp('sp_consulta_aforo_contenedor', (contenedor_id, ruc_cliente), single_row=False)

    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)

@query_bp.route('/inspection/booking', methods=['GET'])
def get_inspection_booking_info():
    """
    6.a. Consulta de Inspecciones por Booking
    """
    booking_id = request.args.get('booking_id')
    ruc_cliente = request.args.get('ruc_cliente')

    if not booking_id or not ruc_cliente:
        return jsonify({"error": "Faltan parámetros requeridos: booking_id, ruc_cliente"}), 400

    data, error = execute_sp('sp_consulta_requerimientos_contenedores_inspeccion', (booking_id, ruc_cliente), single_row=False)

    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)

@query_bp.route('/inspection/container', methods=['GET'])
def get_inspection_container_info():
    """
    6.b. Consulta de Inspecciones por Contenedor
    """
    contenedor_id = request.args.get('contenedor_id')
    ruc_cliente = request.args.get('ruc_cliente')

    if not contenedor_id or not ruc_cliente:
        return jsonify({"error": "Faltan parámetros requeridos: contenedor_id, ruc_cliente"}), 400

    data, error = execute_sp('sp_consulta_inspeccion_contenedor_expo', (contenedor_id, ruc_cliente), single_row=False)

    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)

@query_bp.route('/tally', methods=['GET'])
def get_tally_info():
    """
    7. Consulta de Tarjas (Carga suelta)
    """
    numero_bl = request.args.get('numero_bl')
    ruc_cliente = request.args.get('ruc_cliente')

    if not numero_bl or not ruc_cliente:
        return jsonify({"error": "Faltan parámetros requeridos: numero_bl, ruc_cliente"}), 400

    data, error = execute_sp('sp_consulta_tarja_carga_suelta', (numero_bl, ruc_cliente), single_row=False)

    if error:
        return jsonify({"message": error}), 404 if "No se encontraron datos" in error else 500
    return jsonify(data)
