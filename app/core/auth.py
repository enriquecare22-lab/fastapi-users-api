import os 
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

#--------------------
# configuracion JWT
#-------------------

SECRET_KEY =os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCCES_TOKEN_EXPIRE_MINUTES = 30

#configuracion de encriptacion
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#Password

def hash_password(password:str):
    """
    Encripta la contraseña antes de guardarla.
    proteccion password bcrypt (max 72 chars)
    """
    password = str(password)[:72]
    return pwd_context.hash(password)


def verify_password(plain, hashed):
    """
    compara contraseña ingresada vs encriptada.
    """
    return pwd_context.verify(plain, hashed)



#Token JWT

def create_access_token(data: dict):
    """
    genera un token JWT con expiracion
    """

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes =ACCCES_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)