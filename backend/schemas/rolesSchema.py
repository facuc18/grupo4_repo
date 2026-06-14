from pydantic import BaseModel,ConfigDict

class Rol(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str