from pydantic import BaseModel

#Schemas para crear usuario (entrada)
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

#Schema para respuesta (salida)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_model = True #permite usar objetos de SQLALchemy
        

