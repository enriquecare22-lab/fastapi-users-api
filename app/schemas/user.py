from pydantic import BaseModel

#Schemas para crear usuario (entrada)
class UserCreate(BaseModel):
    name: str
    email: str

#Schema para respuesta (salida)
class UserResponse(UserCreate):
    id: int

    class Config:
        orm_model = True #permite usar objetos de SQLALchemy
        