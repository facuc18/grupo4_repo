from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# conexión a la base de datos
DATABASE_URL = ""

engine = create_engine(DATABASE_URL)

# cada request usa una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base de todos los modelos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()