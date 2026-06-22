from pydantic import BaseModel,ConfigDict

class VendedorInfo(BaseModel):
    id:int
    nombre:str

class PublicacionLista(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    precio: float
    categoria : str

class PublicacionDetalle(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    descripcion: str
    precio: float
    stock: int
    fecha_publicacion: str
    categoria: str
    vendedor:VendedorInfo

class PublicacionCrear(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    titulo: str
    descripcion: str
    precio: float
    stock: int
    categoria_id:int
    vendedor_id:int

class PublicacionActualizar(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    titulo: str | None = None
    descripcion: str | None = None
    precio: float | None = None
    stock: int | None = None
    estado: str | None = None
    categoria: str | None = None

class PublicacionEliminar(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int