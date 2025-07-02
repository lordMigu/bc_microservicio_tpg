# Dockerfile para la aplicación Flask con autenticación JWT y SQL Server

# Etapa 1: Imagen Base
FROM python:3.11-slim

# Configuración del Entorno
WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Instalar dependencias necesarias para Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Configurar FreeTDS
RUN echo "[global]" > /etc/freetds/freetds.conf && \
    echo "tds version = 7.2" >> /etc/freetds/freetds.conf && \
    echo "client charset = UTF-8" >> /etc/freetds/freetds.conf

# Instalación de Dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia del Código de la Aplicación
COPY . .

# Configuración de Red
EXPOSE 5000

# Copiar script de espera
COPY wait-for-sqlserver.py .

# Comando de Ejecución
CMD ["sh", "-c", "python wait-for-sqlserver.py && python -m flask run --host=0.0.0.0 --port=5000"]
