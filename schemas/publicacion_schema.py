from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from database.models import tipo_publicacionEnum
from schemas.user_schema import UserBase

class PublicacionBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    tipo_publicacion: tipo_publicacionEnum
    fecha_publicacion: datetime

class PublicacionCreate(UserBase, PublicacionBase):
    pass

class PublicacionResponse(PublicacionBase):
    id_publicacion: int
    id_usuario: int

    class Config:
        from_attributes = True