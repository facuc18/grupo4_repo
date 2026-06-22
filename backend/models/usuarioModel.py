from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime
from database import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)

    nombre = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    telefono = Column(String(20))

    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    
    rol = relationship("Roles", back_populates="usuarios")
    publicaciones = relationship("Publicacion", back_populates="vendedor")
