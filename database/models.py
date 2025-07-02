class Usuario:
    """
    Clase que representa un usuario en la base de datos.
    """
    def __init__(self, usuario_id, email, password_hash, ruc_cliente, 
                 nombre_cliente, perfil_cliente, estado_cuenta,
                 fecha_creacion=None, ultimo_login=None):
        self.usuario_id = usuario_id
        self.email = email
        self.password_hash = password_hash
        self.ruc_cliente = ruc_cliente
        self.nombre_cliente = nombre_cliente
        self.perfil_cliente = perfil_cliente
        self.estado_cuenta = estado_cuenta
        self.fecha_creacion = fecha_creacion
        self.ultimo_login = ultimo_login

    def to_dict(self):
        """
        Método útil para convertir el objeto Usuario a un diccionario,
        facilitando su conversión a JSON.
        """
        return {
            "usuario_id": self.usuario_id,
            "email": self.email,
            "ruc_cliente": self.ruc_cliente,
            "nombre_cliente": self.nombre_cliente,
            "perfil_cliente": self.perfil_cliente,
            "estado_cuenta": self.estado_cuenta
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Usuario desde un diccionario.
        """
        return cls(
            usuario_id=data.get('usuario_id'),
            email=data.get('email'),
            password_hash=data.get('password_hash'),
            ruc_cliente=data.get('ruc_cliente'),
            nombre_cliente=data.get('nombre_cliente'),
            perfil_cliente=data.get('perfil_cliente'),
            estado_cuenta=data.get('estado_cuenta'),
            fecha_creacion=data.get('fecha_creacion'),
            ultimo_login=data.get('ultimo_login')
        )
