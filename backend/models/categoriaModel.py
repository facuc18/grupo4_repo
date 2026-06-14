from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)

    nombre = Column(
        String(100),
        nullable=False,
        unique=True
    )

    descripcion = Column(Text)

    publicaciones = relationship("Publicacion", back_populates="categoria")