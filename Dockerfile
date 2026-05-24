# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar e instalar dependencias primero (mejor uso del cache de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Cloud Run inyecta la variable PORT automáticamente (por defecto 8080)
ENV PORT=8080

# Comando para iniciar el servidor
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}
