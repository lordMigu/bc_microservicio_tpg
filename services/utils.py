from database.database import get_db
from flask import jsonify, request
from functools import wraps

def execute_sp(sp_name, params, single_row=True):
    """
    Ejecuta un procedimiento almacenado y devuelve los resultados.
    Si params es un diccionario, se asume que los valores están en el orden correcto.
    Si params es una lista/tupla, se asume que los valores están en el orden correcto.
    Si params es None, se ejecuta el procedimiento sin parámetros.
    """
    try: 
        with get_db() as conn:
            with conn.cursor() as cursor:
                # Construir la llamada EXEC soportando diccionario o lista/tupla
                if params: # Si params es un diccionario o lista/tupla
                    if isinstance(params, dict): # Si params es un diccionario
                        # Mantener el orden de inserción (Python 3.7+)
                        placeholders = ', '.join([f"@{k}=?" for k in params.keys()]) # Genera placeholders para cada parámetro
                        query = f"EXEC {sp_name} {placeholders}" # Construye la consulta
                        values = list(params.values())
                    else: # Si params es una lista/tupla
                        # Asumir secuencia en el orden correcto
                        placeholders = ', '.join(['?'] * len(params)) # Genera placeholders para cada parámetro
                        query = f"EXEC {sp_name} {placeholders}" # Construye la consulta
                        values = params
                    cursor.execute(query, values)
                else:
                    cursor.execute(f"EXEC {sp_name}")
                
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


def service_response(data, error=None, custom_code=None, http_status=None):
    """Construye una respuesta estándar para los servicios con códigos personalizados.

    Códigos personalizados:
    - 0: Éxito con datos.
    - 1: No se encontraron datos.
    - 2: Parámetros de solicitud inválidos (Bad Request).
    - 3: Error interno del servidor.
    """
    response = {}
    status_code = 200

    if error:
        # Si el código es 2, es un Bad Request
        if custom_code == 2:
            status_code = http_status or 400
        # Si no hay datos, es un Not Found
        elif "No se encontraron datos" in error:
            status_code = http_status or 404
            custom_code = 1 # Forzar código 1
        # Cualquier otro error es un error de servidor
        else:
            status_code = http_status or 500
            custom_code = 3 # Forzar código 3
        
        response['code'] = custom_code
        response['message'] = error

    elif data is not None and data != []:
        status_code = http_status or 200
        response['code'] = 0
        response['data'] = data
    else:
        status_code = http_status or 404
        response['code'] = 1
        response['message'] = "No se encontraron datos."

    return jsonify(response), status_code

def require_params(*required_args):
    """Decorador para validar que los parámetros requeridos están en la solicitud."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            missing_params = [arg for arg in required_args if arg not in request.args or not request.args.get(arg)]
            if missing_params:
                error_msg = f"Parámetros requeridos faltantes o vacíos: {', '.join(missing_params)}"
                return service_response(None, error_msg, custom_code=2)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Version anterior de execute_sp (estable)
# def execute_sp(sp_name, params, single_row=True):
#     """
#     Ejecuta un procedimiento almacenado y devuelve los resultados.
    
#     Parámetros:
#     - sp_name: El nombre del procedimiento almacenado a ejecutar.
#     - params: Una lista de parámetros para el procedimiento almacenado.
#     - single_row: Un booleano que indica si se espera un solo resultado (True) o una lista de resultados (False).
    
#     Retorna:
#     - Un diccionario con los resultados del procedimiento almacenado si se ejecuta correctamente.
#     - Un error con codigo 404 si el error indica que no se encontraron datos,
#     - Un error con codigo 500 si ocurre un error al ejecutar el procedimiento almacenado.
#     """
#     try:
#         with get_db() as conn:
#             with conn.cursor() as cursor:
#                 placeholders = ', '.join(['?'] * len(params))
#                 cursor.execute(f"EXEC {sp_name} {placeholders}", params)
                
#                 columns = [column[0] for column in cursor.description]
                
#                 if single_row: # Si se espera un solo resultado
#                     row = cursor.fetchone() # Obtiene el primer resultado
#                     if row: # Si se encuentra un resultado
#                         return dict(zip(columns, row)), None # Retorna el resultado como un diccionario
#                     return None, "No se encontraron datos."
#                 else: # Si se espera una lista de resultados
#                     rows = cursor.fetchall() # Obtiene todos los resultados
#                     if rows: # Si se encuentran resultados
#                         return [dict(zip(columns, row)) for row in rows], None # Retorna los resultados como una lista de diccionarios
#                     return [], "No se encontraron datos."
#     except Exception as e: # Si ocurre un error
#         return None, str(e) # Retorna el error