from database.database import get_db

def execute_sp(sp_name, params, single_row=True):
    """
    Ejecuta un procedimiento almacenado y devuelve los resultados.
    """
    try:
        with get_db() as conn:
            with conn.cursor() as cursor:
                placeholders = ', '.join(['?'] * len(params))
                cursor.execute(f"EXEC {{sp_name}} {{placeholders}}", params)
                
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
