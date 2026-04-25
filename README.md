# 🚀 FastAPI Backend - Users API

API backend desarrollada con **FastAPI** y **PostgreSQL** que permite gestionar usuarios.

## 📌 Características

* Crear usuarios
* Listar usuarios
* Conexión a base de datos PostgreSQL
* Arquitectura básica profesional
* Validación de datos con Pydantic

---

## 🛠 Tecnologías utilizadas

* Python 3
* FastAPI
* Uvicorn
* SQLAlchemy
* PostgreSQL

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

## 🌐 Endpoints

### GET /

* Verifica que la API está funcionando

### POST /users

* Crear usuario

Ejemplo:

```json
{
  "name": "Juan",
  "email": "juan@email.com"
}
```

### GET /users

* Obtener lista de usuarios

---

## 📚 Documentación automática

FastAPI genera documentación en:

👉 http://127.0.0.1:8000/docs

---

## 📁 Estructura del proyecto

```
app/
│
├── main.py        # Punto de entrada
├── database.py    # Configuración DB
├── models.py      # Modelos SQLAlchemy
├── schemas.py     # Validaciones Pydantic
```

---

## 🚀 Próximas mejoras

* Autenticación JWT
* Relaciones entre tablas
* Deploy en la nube
* Tests automatizados

---

## 👨‍💻 Autor Enrique C. R.
Desarrollado como parte de aprendizaje de backend con FastAPI.
