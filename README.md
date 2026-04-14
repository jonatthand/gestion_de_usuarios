[![Coverage Status](https://coveralls.io/repos/github/jonatthand/gestion_de_usuarios/badge.svg)](https://coveralls.io/github/jonatthand/gestion_de_usuarios)

# 📦 Notification Management API

API REST desarrollada con **FastAPI** para la gestión y envío de notificaciones multicanal (Email, SMS y Push), aplicando buenas prácticas de arquitectura, testing y despliegue.

---

## 🚀 Features

* 📬 Creación y gestión de notificaciones
* 📡 Envío por múltiples canales:

  * Email
  * SMS
  * Push
* 🧠 Patrón Strategy + Factory para selección de canal
* 🧪 Tests unitarios con mocks
* 🐳 Contenerización con Docker
* 🔄 CI con GitHub Actions
* 📊 Coverage con Coveralls
* ☁️ Deploy en Render

---

## 🧱 Arquitectura

El proyecto sigue principios de **Clean Architecture**:

```
src/
├── auth/
├── core/
├── notifications/
│   ├── controllers/
│   ├── services/
│   ├── repositories/
│   ├── strategies/
│   ├── models/
├── tests/
```

### Capas:

* **Controllers** → Manejo de requests (FastAPI routers)
* **Services** → Lógica de negocio
* **Repositories** → Acceso a datos
* **Strategies** → Envío por canal (Email, SMS, Push)

---

## 🧠 Decisiones técnicas

* Uso de **Strategy Pattern** para desacoplar canales de envío
* Uso de **Factory Pattern** para selección dinámica del sender
* Inyección de dependencias para facilitar testing (sin **patch**)
* Separación clara de responsabilidades (SRP)

---

## 🛠️ Tecnologías

* Python 3.11+
* FastAPI
* SQLAlchemy
* SQLite
* Pytest
* Docker
* GitHub Actions

---

## ⚙️ Instalación local

### 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/gestion_de_usuarios.git
cd gestion_de_usuarios
```

---

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar la app

```bash
uvicorn src.main:app --reload
```

---

### 5. Documentación interactiva

```
http://localhost:8000/docs
```

---

## 🐳 Docker

### Build y run:

```bash
docker compose up --build
```

---

## 🧪 Testing

Ejecutar tests:

```bash
pytest
```

Con coverage:

```bash
pytest --cov=src
```

---

## 🧪 Estrategia de testing

* Uso de **pytest**
* Uso de **MagicMock** para simular dependencias
* Tests aislados del entorno (sin DB real ni servicios externos)

---

## 🔄 CI/CD

El proyecto incluye integración continua con GitHub Actions:

* Instalación de dependencias
* Ejecución de tests
* Generación de coverage

---

## 📊 Coverage

El coverage del proyecto se reporta mediante Coveralls.

---

## ☁️ Deploy

API desplegada en Render:

```
https://gestion-de-usuarios-pums.onrender.com/docs
```

---

## ⚠️ Notas

* SQLite utilizado para simplificar el entorno
* Render en plan free puede tener latencia inicial (cold start)

---

## 📌 Mejoras futuras

* Autenticación con JWT completa
* Manejo de colas (RabbitMQ / Redis)
* Persistencia en PostgreSQL
* Rate limiting
* Logs estructurados

---

## 👤 Autor

Jonathan

---

## 🧠 Conclusión

Este proyecto demuestra:

* Aplicación de patrones de diseño
* Separación de responsabilidades
* Testing robusto
* Preparación para producción
* Despliegue real en la nube

---
