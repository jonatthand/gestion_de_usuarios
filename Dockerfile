# Imagen base
FROM python:3.11-slim

# Evita crear archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Logs inmediatos
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer puerto
EXPOSE 8000

# Comando para correr la app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]