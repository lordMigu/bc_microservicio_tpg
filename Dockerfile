# Dockerfile para la aplicación Flask con autenticación JWT y SQL Server

# Etapa 1: Imagen Base
FROM python:3.11-slim

# Configuración del Entorno
WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Actualizar e instalar dependencias del sistema para el driver ODBC de Microsoft
# --- DRIVER PARA SQL SERVER (ACTUAL) ---
# Descomentar estas líneas para usar el driver oficial de Microsoft para SQL Server
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl -sSL -O https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

# --- DRIVER PARA SYBASE (ALTERNATIVA) ---
# Descomentar esta línea para usar FreeTDS (compatible con Sybase) y comentar las de SQL Server
# RUN apt-get update && apt-get install -y freetds-dev freetds-bin unixodbc-dev

# Instalación de Dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia del Código de la Aplicación
COPY . .

# Configuración de Red
EXPOSE 5000

# Comando de Ejecución
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
