from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from database.database import get_db
from database.models import Usuario

# Documento de referencia: Inicio de sesión , Administración de Cuenta 
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint para el inicio de sesión del usuario.
    Valida las credenciales contra la base de datos usando pytds.
    """
    # Se obtienen los datos JSON de la petición (email y password)
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Faltan email o password"}), 400

    email = data.get('email')
    password = data.get('password')

    # Se obtiene una conexión a la base de datos
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Consulta para obtener el usuario
        cursor.execute("""
            SELECT UsuarioID, Email, PasswordHash, RucCliente, NombreCliente,
                   PerfilCliente, EstadoCuenta, FechaCreacion, UltimoLogin
            FROM Usuarios
            WHERE Email = ?
        """, email)
        
        # Obtener el resultado
        row = cursor.fetchone()
        
        if not row:
            return jsonify({"msg": "Usuario o contraseña incorrectos"}), 401

        # Crear objeto Usuario desde los datos obtenidos
        user_in_db = Usuario.from_dict({
            'usuario_id': row[0],
            'email': row[1],
            'password_hash': row[2],
            'ruc_cliente': row[3],
            'nombre_cliente': row[4],
            'perfil_cliente': row[5],
            'estado_cuenta': row[6],
            'fecha_creacion': row[7],
            'ultimo_login': row[8]
        })

        # Verificar la contraseña
        if user_in_db.password_hash != password:
            return jsonify({"msg": "Usuario o contraseña incorrectos"}), 401

        # Verificar el estado de la cuenta
        if user_in_db.estado_cuenta == 'Inactiva':
            return jsonify({"msg": "La cuenta está desactivada. Por favor, contacte a soporte."}), 403
        
        if user_in_db.estado_cuenta == 'PendienteAprobacion':
            return jsonify({"msg": "Su cuenta aún no ha sido aprobada."}), 403

        # Si todo está bien, se genera el token JWT
        identity_data = {
            "email": user_in_db.email,
            "ruc": user_in_db.ruc_cliente,
            "perfil": user_in_db.perfil_cliente
        }
        access_token = create_access_token(identity=identity_data)

        # Se devuelve el token y datos básicos del usuario.
        return jsonify(
            access_token=access_token,
            user=user_in_db.to_dict()
        )
    return jsonify(
        access_token=access_token,
        user=user_in_db.to_dict()
    )

@auth_bp.route('/register', methods=['POST'])
def register():
    # Se usa la opción “Register” del sistema TPG SSO para crear el usuario. 
    # Adicionalmente se crea la Solicitud de Aprobación de Usuario. 
    return jsonify({"message": "Solicitud de registro enviada para aprobación."}), 202

@auth_bp.route('/activate-account', methods=['POST'])
@jwt_required()
def activate_account():
    # Integración: Llamado al “API-TPG Servicio_Activar_Cuenta” 
    # Este servicio crea la Solicitud de Activación de Usuario de App. 
    return jsonify({"message": "Solicitud de activación de cuenta enviada."}), 202

@auth_bp.route('/deactivate-account', methods=['POST'])
@jwt_required()
def deactivate_account():
    # Integración: Llamado al “API-TPG Servicio_Desactivar_Cuenta” 
    # Este servicio crea la Solicitud de Desactivación de Usuario de App. 
    return jsonify({"message": "Solicitud de desactivación de cuenta enviada."}), 202

@auth_bp.route('/change-password', methods=['POST'])
@jwt_required()
def change_password():
    # Integración: Se Redirige con un Token de Aplicación a TPG SSO (KEYCLOACK). 
    return jsonify({"message": "Redirigiendo para cambiar la contraseña."})