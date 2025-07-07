# Dockerfile que instala en el contenedor todas las dependencias necesarias para que la aplicación funcione
# python 3.11-slim es más ligero que la imagen base de python 3.11
# ENV PYTHONUNBUFFERED=1 deshabilita el buffer de la salida de Python para que se vea la salida en el terminal
# Se debe comentar la línea de la base de datos que no se desea usar
# Se debe descomentar la línea de la base de datos que se desea usar
# CMD hace lo siguiente: 
# Ejecuta el comando python -m flask run --host=0.0.0.0 --port=5000
# para que la aplicación se ejecute en el contenedor en el puerto 5000

# Etapa 1: Imagen Base
FROM python:3.11-slim

# Configuración del Entorno
WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Actualizar e instalar dependencias del sistema para el driver ODBC de Microsoft
# --- DRIVER PARA SQL SERVER ---
# Descomentar estas líneas para usar el driver oficial de Microsoft para SQL Server
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl -sSL -O https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

# --- DRIVER PARA SYBASE SAP ASE 16 ---
# Para conectar a Sybase, comenta el bloque anterior de SQL Server y descomenta la siguiente línea.
# Esto instalará FreeTDS, un driver compatible con Sybase.
# Instala los drivers necesarios para Sybase y limpia la caché de apt
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     freetds-dev \
#     unixodbc-dev \
#     tdsodbc \
#     freetds-bin \
#     nmap \
#     && rm -rf /var/lib/apt/lists/*
# Comentar/Descomentar si se usara o no SYBASE
# Copiar configuración personalizada de FreeTDS para SAP ASE 16.1
# COPY freetds.conf /etc/freetds/freetds.conf
# Configurar el driver FreeTDS para que unixODBC pueda encontrarlo.
# Configurar odbcinst.ini para que apunte a la ubicación correcta del controlador
# RUN echo "[FreeTDS]\nDescription = FreeTDS Driver\nDriver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\nSetup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" > /etc/odbcinst.ini

# Crear el archivo odbc.ini con la configuración de la conexión
# RUN echo "[SAPASE_HOST]\nDriver = FreeTDS\nDescription = SAP ASE Connection\nServer = host.docker.internal\nPort = 5000\nTDS_Version = 4.2\n" > /etc/odbc.ini

# Instalación de Dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia del Código de la Aplicación
COPY . .

# Configuración de Red
EXPOSE 5000

# Comando de Ejecución
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
