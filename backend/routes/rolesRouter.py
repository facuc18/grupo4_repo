from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from models.rolesModel import Roles
from database  import get_db

router = APIRouter()

@router.get("/roles")
def get_roles(db:Session = Depends(get_db)):
    roles = db.query(Roles).all()

    return roles