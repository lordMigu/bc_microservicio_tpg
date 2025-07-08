# Dockerfile que instala en el contenedor todas las dependencias necesarias para que la aplicación funcione
# python 3.11-slim es más ligero que la imagen base de python 3.11
# ENV PYTHONUNBUFFERED=1 deshabilita el buffer de la salida de Python para que se vea la salida en el terminal
# Se debe comentar la línea de la base de datos que no se desea usar
# Se debe descomentar la línea de la base de datos que se desea usar
# CMD hace lo siguiente: 
# Ejecuta el comando python -m flask run --host=0.0.0.0 --port=5000
# para que la aplicación se ejecute en el contenedor por el puerto 5000

# Medidas de seguridad implementadas:
# 1. Creación y uso de un usuario no-root ('appuser').
# 2. Actualización de paquetes del sistema para parches de seguridad.
# 3. Asignación de permisos de archivos correctos al usuario no-root.
# 4. Inclusión de un HEALTHCHECK para monitorear el estado de la aplicación.

# Etapa 1: Imagen Base
FROM python:3.11-slim

# Configuración del Entorno
WORKDIR /app
ENV PYTHONUNBUFFERED=1

# --- Medida de Seguridad: Crear un usuario no-root ---
# Se crea un usuario y grupo 'appuser' sin privilegios de root.
# Ejecutar el contenedor como no-root es una práctica de seguridad fundamental.
RUN addgroup --system appuser && adduser --system --ingroup appuser appuser

# --- DRIVER PARA SQL SERVER ---
# Descomentar estas líneas para usar el driver oficial de Microsoft para SQL Server.
# --- Medida de Seguridad: Actualizar paquetes y limpiar ---
# Se añade 'apt-get upgrade -y' para instalar las últimas actualizaciones de seguridad.
# Se limpian los archivos de apt en la misma capa RUN para reducir el tamaño de la imagen.
# RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends curl gnupg && \
#     curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
#     curl -sSL -O https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb && \
#     dpkg -i packages-microsoft-prod.deb && \
#     rm packages-microsoft-prod.deb && \
#     apt-get update && \
#     ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# --- DRIVER PARA SYBASE SAP ASE 16 ---
# Para conectar a Sybase, comenta el bloque anterior de SQL Server y descomenta las siguientes líneas.
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    freetds-dev \
    unixodbc-dev \
    tdsodbc \
    freetds-bin \
    nmap \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY freetds.conf /etc/freetds/freetds.conf
RUN echo "[FreeTDS]\nDescription = FreeTDS Driver\nDriver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\nSetup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" > /etc/odbcinst.ini
RUN echo "[SAPASE_HOST]\nDriver = FreeTDS\nDescription = SAP ASE Connection\nServer = host.docker.internal\nPort = 5000\nTDS_Version = 4.2\n" > /etc/odbc.ini

# Instalación de Dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia del Código de la Aplicación
COPY . .

# --- Medida de Seguridad: Asignar permisos al usuario no-root ---
# Se cambia el propietario del directorio de la aplicación al usuario 'appuser'.
RUN chown -R appuser:appuser /app

# --- Medida de Seguridad: Cambiar al usuario no-root ---
# Se cambia al usuario 'appuser' para ejecutar la aplicación.
USER appuser

# Configuración de Red
EXPOSE 5000

# --- Medida de Seguridad: Healthcheck ---
# Se añade un HEALTHCHECK para que Docker pueda verificar el estado de la aplicación.
# Nota: Esto requiere que la aplicación tenga un endpoint '/health' que devuelva un estado 200 OK.
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# Comando de Ejecución
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
