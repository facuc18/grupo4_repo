from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from models.categoriaModel import Categoria
from database  import get_db

from schemas.categoriaSchema import CategoriaSchema

router = APIRouter()

@router.get("/categorias", response_model=list[CategoriaSchema])
def get_categorias(db:Session = Depends(get_db)):
    categorias = db.query(Categoria).all()

    return categorias