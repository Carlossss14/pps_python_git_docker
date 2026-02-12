# ---------- FASE 1: build / resolución de dependencias ----------
FROM python:3.10-slim AS builder

# Establecer directorio de trabajo
WORKDIR /app

# Copiar solo los ficheros necesarios para instalar dependencias
COPY requirements.txt .

# Instalar dependencias en un directorio aislado
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- FASE 2: runtime / ejecución ----------
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias instaladas desde la fase builder
COPY --from=builder /install /usr/local

# Copiar el código de la aplicación
COPY app.py bayeta.py frases.txt ./

# Exponer el puerto donde corre Flask
EXPOSE 5000

# Variable de entorno para que Flask escuche en todas las interfaces
ENV FLASK_APP=app.py

# Comando de ejecución
CMD ["python", "app.py"]
