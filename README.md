![Coverage Status](https://coveralls.io/repos/github/jonatthand/gestion_de_usuario/badge.svg)

# Notification Service API

## Overview

Notification Service es una API desarrollada en **FastAPI** que permite crear y enviar notificaciones a través de múltiples canales (email, SMS y push).
El proyecto implementa una arquitectura modular basada en **capas y patrones de diseño**, lo que facilita su escalabilidad y mantenimiento.

La aplicación incluye:

* Autenticación basada en **JWT**
* Persistencia en base de datos
* Envío de notificaciones mediante diferentes **estrategias**
* Documentación automática con **Swagger**

Este proyecto fue desarrollado como parte de un **technical challenge**, priorizando buenas prácticas de diseño y claridad en la arquitectura.

---

# Architecture

La aplicación sigue una **arquitectura por capas**, separando responsabilidades para mantener el código limpio y mantenible.

```
Controller (API layer)
        ↓
Service (business logic)
        ↓
Repository (data access)
        ↓
Database
```

Además, el envío de notificaciones utiliza el **Strategy Pattern**, permitiendo cambiar el comportamiento según el canal de envío sin modificar la lógica principal.

```
SenderService
      ↓
 ┌───────────────┬───────────────┬───────────────┐
 EmailSender     SMSSender       PushSender
```

Esto permite agregar nuevos canales de notificación sin modificar el servicio principal.

---

# Tech Stack

* **Python 3.11+**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **JWT Authentication**
* **Uvicorn**
* **SQLite** (puede reemplazarse fácilmente por PostgreSQL)

---

# Project Structure

```
src/
│
├── auth
│   ├── controllers
│   ├── services
│   └── schemas
│
├── notifications
│   ├── controllers
│   ├── services
│   ├── repositories
│   ├── strategies
│   └── schemas
│
├── database
│
└── main.py
```

Descripción de carpetas principales:

| Folder       | Description                                          |
| ------------ | ---------------------------------------------------- |
| controllers  | Manejo de endpoints HTTP                             |
| services     | Lógica de negocio                                    |
| repositories | Acceso a base de datos                               |
| strategies   | Implementación del Strategy Pattern para los canales |
| schemas      | Modelos Pydantic para validación                     |

---

# Installation

Clonar el repositorio:

```bash
git clone https://github.com/your-username/notification-service.git
cd notification-service
```

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar entorno:

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Iniciar el servidor con **Uvicorn**:

```bash
uvicorn src.main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI genera documentación automática.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Redoc:

```
http://127.0.0.1:8000/redoc
```

---

# Authentication

La API utiliza **JWT (JSON Web Tokens)** para autenticación.

Flujo básico:

1. Registrarse o iniciar sesión
2. Obtener un **access token**
3. Incluir el token en los requests

Header requerido:

```
Authorization: Bearer <token>
```

---

# API Endpoints

## Auth

### Register user

```
POST /auth/register
```

### Login

```
POST /auth/login
```

Devuelve un token JWT.

---

## Notifications

### Create notification

```
POST /notifications/notifications
```

Example request:

```json
{
  "title": "Test notification",
  "message": "This is a test",
  "channel": "email",
  "recipient": "user@example.com"
}
```

Possible channels:

```
email
sms
push
```

---

### Get notifications

```
GET /notifications/notifications
```

Devuelve todas las notificaciones del usuario autenticado.

---

# Notification Status

Las notificaciones pueden tener los siguientes estados:

| Status  | Description                               |
| ------- | ----------------------------------------- |
| created | La notificación fue creada                |
| sent    | La notificación fue enviada correctamente |
| failed  | Ocurrió un error durante el envío         |

---

# Strategy Pattern Implementation

El envío de notificaciones se maneja mediante el **Strategy Pattern**.

Esto permite que el servicio seleccione dinámicamente el método de envío según el canal.

Ejemplo simplificado:

```
SenderService
     ↓
Select Strategy
     ↓
EmailSender / SMSSender / PushSender
```

Beneficios:

* Código desacoplado
* Fácil extensión
* Mejor mantenibilidad

---

# Example Workflow

1. Usuario autenticado crea una notificación.
2. El sistema la guarda en la base de datos.
3. Se selecciona la estrategia de envío según el canal.
4. La notificación se envía.
5. Se actualiza el estado (`sent` o `failed`).

---

# Possible Improvements

Algunas mejoras posibles para una versión productiva:

* Cola de mensajes (RabbitMQ / Redis / Kafka)
* Workers para envío asincrónico
* Retries automáticos
* Rate limiting
* Tests automatizados con pytest
* Dockerización

---

# Frontend (Optional)

El proyecto puede incluir un frontend simple para consumir los endpoints de la API, permitiendo:

* Login
* Crear notificaciones
* Listar notificaciones

Esto facilita probar el sistema de manera visual.

---

# Author

Jonathan Daniel

Backend Developer
