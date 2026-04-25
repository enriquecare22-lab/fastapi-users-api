from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.user_service import create_user, login_user, get_all_users

# ROUTER (NDPOINTS)
#---------------

router = APIRouter()

#Dependecy para obtener conexion a DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#REGISTER
print("estoy aqui")
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    print(register)
    """
    Endpoit para registrar usuario
    """
    new_user = create_user(db, user.name, user.email, user.password)
    if not new_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    return {"message" : "Usuario creado correctamente" }

#LOGIN

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Endpoint de autenticacion
    Devueleve JWT si las credenciales son correctas
    """
    token = login_user(db, user.email, user.password)

    if not token:
        raise HTTPException(status_code = 400, detail="Credenciales inválidas")
    
    return {
        "access_token": token,
        "token_type": "bearer"
        }


#Listar Usuarios

@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    """
    Devueleve lista de usuarios (sin password)
    """
    return get_all_users(db)

