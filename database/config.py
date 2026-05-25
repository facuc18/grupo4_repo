# database/config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

# Configuración de conexión
DATABASE_URL = "postgresql://user:password@localhost:5432/agromarket"

# Crear engine
engine = create_engine(
    DATABASE_URL,
    pool_size=10,  # Tamaño del pool de conexiones
    max_overflow=20,  # Conexiones extras permitidas
    pool_pre_ping=True,  # Verificar conexiones antes de usarlas
    echo=False  # Cambiar a True para ver SQL generado
)

# Crear session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para FastAPI
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para crear tablas
def create_tables():
    from database.models import Base
    Base.metadata.create_all(bind=engine)

# Función para eliminar tablas (útil para pruebas)
def drop_tables():
    from database.models import Base
    Base.metadata.drop_all(bind=engine)