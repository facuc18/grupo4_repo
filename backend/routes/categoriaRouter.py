from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from models.categoriaModel import Categoria
from database  import get_db

router = APIRouter()

@router.get("/categorias")
def get_categorias(db:Session = Depends(get_db)):
    categorias = db.query(Categoria).all()

    return categorias