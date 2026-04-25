from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

#importamos la conexion a base de datos
from app.database import engine, Base,SessionLocal

#importamos modelos y schemas
from app import models
from app.models import User
from app.schemas import UserCreate

#Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

#inicializar app
app = FastAPI()

#Dependency para obtener conexion a la base de datos
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Endpoint raiz(prueba)
@app.get("/")
def home():
    return {"message": "API funciona correctamente"}

#crear usuario
@app.post("/users")
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    new_user = User(name=user.name, email=user.email)

    #guardar en DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
#Obtener todos los usuarios
@app.get("/users")
def get_users(db: Session=Depends(get_db)):
    return db.query(User).all()
