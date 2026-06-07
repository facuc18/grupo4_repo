from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from database import Base

class Leasing(Base):

    __tablename__ = "leassings"

    id = Column(Integer, primary_key=True)

    fecha_solicitud = Column(DateTime,default=datetime.utcnow)

    cantidad_cuotas = Column(
        Integer,
        nullable=False
    )

    monto_total = Column(
        Numeric(12,2),
        nullable=False
    )

    estado = Column(
        String(20),
        nullable=False
    )

    comprador_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    publicacion_id = Column(
        Integer,
        ForeignKey("publicaciones.id"),
        nullable=False
    )