from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime
from database import Base

class Usuario(Base):
    id = Column(Integer, primary_key=True)

    nombre = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    telefono = Column(String(20))

    tipo_usuario = Column(
        String(20),
        nullable=False
    )