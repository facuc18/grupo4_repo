from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from database.models import TipoMaquinariaEnum, EstadoMaquinariaEnum
from schemas.product_schema import ProductBase


class MaquinariaBase(BaseModel):
    tipo: TipoMaquinariaEnum
    marca:str
    modelo:str
    year:int
    estado: EstadoMaquinariaEnum

class MaquinariaCreate(ProductBase, MaquinariaBase):
    pass

class MaquinariaResponse(MaquinariaBase):
    id_maquinaria : int
  
    id_producto : int

    class Config:
        from_attributes = True
  