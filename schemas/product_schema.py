from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from schemas.publicacion_schema import PublicacionBase


class ProductBase(BaseModel):
    nombre: str
    stock: int
    precio: float


class ProductCreate(PublicacionBase, ProductBase):
    pass


class ProductResponse(ProductBase):
    id_producto: int

    id_publicacion: int

    class Config:
        from_attributes = True