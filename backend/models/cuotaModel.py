
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric
from database import Base

class Cuota(Base):

    __tablename__ = "cuotas"

    id = Column(Integer, primary_key=True)

    numero_cuota = Column(
        Integer,
        nullable=False
    )

    monto = Column(
        Numeric(12,2),
        nullable=False
    )

    pagada = Column(
        Boolean,
        default=False
    )

    fecha_vencimiento = Column(DateTime)

    leasing_id = Column(
        Integer,
        ForeignKey("leasing.id"),
        nullable=False
    )