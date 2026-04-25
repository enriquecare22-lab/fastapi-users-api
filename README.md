# 🚀 FastAPI Backend - Users API

API backend desarrollada con **FastAPI** y **PostgreSQL** que permite gestionar usuarios.
implementa autenticacion de usuarios con JWT, arquitectura modular y conexion a base de datos PostgreSQL.

## 📌 Características

* Registro de usuarios
* Login con autenticación JWT
* Hash seguro de contraseñas (bcrypt)
* Arquitectura profesional (routers, services, models, schemas)
* Validación de datos con Pydantic
* Conexión a PostgreSQL con SQLAlchemy
* Variables de entorno con .env

---
🧱 Estructura del proyecto
app/
│
├── main.py              # Punto de entrada
├── database.py          # Configuración de DB
│
├── core/                # Seguridad y configuración
│   └── auth.py
│
├── models/              # Modelos SQLAlchemy
│   └── user.py
│
├── schemas/             # Validación (Pydantic)
│   └── user.py
│
├── services/            # Lógica de negocio
│   └── user_service.py
│
├── routers/             # Endpoints
│   └── user.py

## 🛠 Tecnologías utilizadas

FastAPI
SQLAlchemy
PostgreSQL
Pydantic
Passlib
Python-JOSE

---

## ⚙️ Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

* Windows:

```bash
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```


🔐 Variables de entorno

-------------------------------
Crear archivo .env:

DATABASE_URL=postgresql://postgres:TU_PASSWORD@localhost/fastapi_db
SECRET_KEY=tu_clave_secreta
---

### 4. Configurar base de datos

Asegúrate de tener PostgreSQL corriendo y crea la base de datos:

```sql
CREATE DATABASE fastapi_db;
```

Configura la conexión en:

```python
DATABASE_URL = "postgresql://usuario:password@localhost/fastapi_db"
```

---

### 5. Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

---



ENDPOINTS

#📝 Registro

POST /register

{
  "name": "Enrique",
  "email": "test@test.com",
  "password": "123456"
}
🔐 Login

POST /login

{
  "email": "test@test.com",
  "password": "123456"
}

Respuesta:

{
  "access_token": "...",
  "token_type": "bearer"
}
📋 Obtener usuarios

GET /users

🔐 Seguridad
Contraseñas hasheadas con bcrypt
Tokens JWT con expiración
Validación de longitud de password
Exclusión de password en respuestas


## 📚 Documentación automática

FastAPI genera documentación en:

👉 http://127.0.0.1:8000/docs


---

🚀 Próximas mejoras
Protección de rutas con JWT (Depends)
Roles de usuario (admin/user)
Tests automatizados
Deploy en la nube (Render / Railway)
Migraciones con Alembic


## 👨‍💻 Autor
Desarrollado como parte de aprendizaje de backend con FastAPI.
