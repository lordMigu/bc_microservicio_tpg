"""Archivo principal de la aplicación Flask
Configura y registra todos los servicios de la aplicación"""

from flask import Flask
from config import Config

def create_app():
    """
    Función de fábrica para crear la aplicación Flask
    Configura la aplicación y registra todos los blueprints
    """
    app = Flask(__name__)
    # Carga la configuración desde el archivo config.py y lo hace global para que pueda ser accedido desde cualquier parte de la aplicación
    app.config.from_object(Config)

    # Importar y registrar blueprints
    # Cada servicio tiene su propio blueprint con rutas específicas
    from services.order_service.notificaciones import notifications_bp
    from services.payment_service.gestion_financiera import finanzas_bp
    from services.order_service.servicios_complementarios import servicios_complementarios_bp
    from services.order_service.consultas import consulta_info_bp
    from services.order_service.auxiliares import auxiliares_bp
    from services.payment_service.tarifarios import tarifarios_bp
    from services.order_service.aforo_inspeccion import aforo_inspeccion_bp

    # Registrar los blueprints con sus respectivos prefijos URL
    # Cada servicio tiene su propio espacio de nombres en la URL
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(finanzas_bp, url_prefix='/finanzas')
    app.register_blueprint(servicios_complementarios_bp, url_prefix='/servicios_complementarios')
    app.register_blueprint(consulta_info_bp, url_prefix='/consulta_info')
    app.register_blueprint(auxiliares_bp, url_prefix='/auxiliares')
    app.register_blueprint(tarifarios_bp, url_prefix='/tarifarios')
    app.register_blueprint(aforo_inspeccion_bp, url_prefix='/aforo_inspeccion')

    return app

if __name__ == '__main__':
    """
    Punto de entrada principal de la aplicación
    Solo se ejecuta cuando se ejecuta directamente el archivo
    """
    app = create_app()
    # Ejecutar la aplicación en modo debug
    app.run(debug=True)