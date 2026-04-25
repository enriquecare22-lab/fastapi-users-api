import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#cargar variable de entorno
load_dotenv()


#Obtener URL desde .env
DATABASE_URL = os.getenv("DATABASE_URL")

#crear engine (conexion)
engine = create_engine(DATABASE_URL)

#crea sesion de DB
SessionLocal =sessionmaker(bind=engine)

#Base para modelos
Base = declarative_base()
