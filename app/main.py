from fastapi import FastAPI
from app.database import Base, engine
from app.models import user
from app.routers.user import router as user_router


#APP PRINCIPAl

app = FastAPI()

#crea tablas (solo desarrollo)
Base.metadata.create_all(bind=engine)


#Inlcuir rutas de usuario
app.include_router(user_router)


@app.get("/")
def root():
    """
    Enpoint de prueba
    """
    return {"message": "Api funcionando correctamente"}
