from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from database import Base

class Compra (Base):
    id = Column(Integer, primary_key=True)

    fecha_compra = Column(DateTime,default=datetime.utcnow)

    monto_total = Column(
        Numeric(12,2),
        nullable=False
    )

    estado_pago = Column(
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