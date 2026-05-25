from pydantic import BaseModel
from typing import Optional

from database.models import EspecieEnum


class AnimalBase(BaseModel):

    especie: EspecieEnum

    raza: Optional[str] = None

    peso: int

    edad: int




class AnimalCreate(AnimalBase):

    id_producto: int




class AnimalResponse(AnimalBase):

    id_animal: int

    id_producto: int

    class Config:

        from_attributes = True