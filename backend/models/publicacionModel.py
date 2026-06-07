from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Text
from database import Base

class Publicacion(Base):

    __tablename__ = "publicaciones"

    id = Column(Integer, primary_key=True)

    titulo = Column(
        String(150),
        nullable=False
    )

    descripcion = Column(
        Text,
        nullable=False
    )

    precio = Column(
        Numeric(12,2),
        nullable=False
    )

    stock = Column(
        Integer,
        nullable=False,
        default=1
    )

    estado = Column(
        String(20),
        nullable=False,
        default="ACTIVA"
    )

    fecha_publicacion = Column(
        DateTime,default=datetime.utcnow
    )

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=False
    )

    vendedor_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )