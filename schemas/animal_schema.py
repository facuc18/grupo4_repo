from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from database.models import EspecieEnum
from schemas.product_schema import ProductBase


class AnimalBase(BaseModel):
    especie: EspecieEnum
    raza: Optional[str] = None
    peso: int
    edad:int

class AnimalCreate(ProductBase,AnimalBase):
    pass

class AnimalResponse(AnimalBase):
    id_animal : int
  
    id_producto : int

    class Config:
        from_attributes = True