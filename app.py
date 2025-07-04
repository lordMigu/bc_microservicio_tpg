# Archivo principal de la aplicación Flask
# Configura y registra todos los servicios de la aplicación

from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config

def create_app():
    """
    Función de fábrica para crear la aplicación Flask
    Configura la aplicación y registra todos los blueprints
    """
    app = Flask(__name__)
    # Carga la configuración desde el archivo config.py
    app.config.from_object(Config)
    # Inicializa el manejador JWT para la autenticación
    jwt = JWTManager(app)

    # Importar y registrar blueprints
    # Cada servicio tiene su propio blueprint con rutas específicas
    from services.auth.routes import auth_bp
    from services.traceability.importer import traceability_importer_bp
    from services.traceability.exporter import traceability_exporter_bp
    from services.complementary_services.importer import complementary_importer_bp
    from services.complementary_services.exporter import complementary_exporter_bp
    from services.statistics.routes import statistics_bp
    from services.notifications.routes import notifications_bp
    from services.financial.routes import financial_bp
    from services.query.routes import query_bp

    # Registrar los blueprints con sus respectivos prefijos URL
    # Cada servicio tiene su propio espacio de nombres en la URL
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(traceability_importer_bp, url_prefix='/traceability/importer')
    app.register_blueprint(traceability_exporter_bp, url_prefix='/traceability/exporter')
    app.register_blueprint(complementary_importer_bp, url_prefix='/complementary-services/importer')
    app.register_blueprint(complementary_exporter_bp, url_prefix='/complementary-services/exporter')
    app.register_blueprint(statistics_bp, url_prefix='/statistics')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(financial_bp, url_prefix='/financial')
    app.register_blueprint(query_bp, url_prefix='/query')

    return app

if __name__ == '__main__':
    """
    Punto de entrada principal de la aplicación
    Solo se ejecuta cuando se ejecuta directamente el archivo
    """
    app = create_app()
    # Ejecutar la aplicación en modo debug
    app.run(debug=True)