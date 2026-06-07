from sqlalchemy import Column, Integer, String, Text
from database import Base

class Categoria(Base):
    id = Column(Integer, primary_key=True)

    nombre = Column(
        String(100),
        nullable=False,
        unique=True
    )

    descripcion = Column(Text)