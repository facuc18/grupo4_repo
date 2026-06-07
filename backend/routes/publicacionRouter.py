from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from database  import get_db

router = APIRouter()

@router.get("/publicaciones")
def traer_publicaciones(db:Session = Depends(get_db)):
    pass

@router.get("/publicaciones/{id}")
def detalles_publicaciones(id:int,db:Session = Depends(get_db)):
    pass
