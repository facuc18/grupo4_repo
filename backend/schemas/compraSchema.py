
from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ==========================
# Schema base
# ==========================

class CompraBase(BaseModel):
    publicacion_id: int


# ==========================
# Crear compra
# ==========================

class CompraCreate(CompraBase):
    pass


# ==========================
# Actualizar estado de pago
# ==========================

class CompraEstadoUpdate(BaseModel):
    estado_pago: str


# ==========================
# Respuesta de compra
# ==========================

class CompraResponse(BaseModel):
    id: int
    fecha_compra: datetime
    monto_total: float
    estado_pago: str
    comprador_id: int
    publicacion_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================
# Lista de compras
# ==========================

class CompraListResponse(BaseModel):
    compras: list[CompraResponse]

    model_config = ConfigDict(
        from_attributes=True
    )