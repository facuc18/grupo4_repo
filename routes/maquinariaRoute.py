from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from core.config import get_db

from database.models import (
    Animal,
    Product,
    Machinery
)

from schemas.animal_schema import AnimalCreate, AnimalResponse
from schemas.maquinaria_schema import (
    MaquinariaCreate,
    MaquinariaResponse
)

router = APIRouter(
    prefix="/machinery",
    tags=["Machinery"]
)

#==========================================POST=========================================
@router.post(
    "/",
    response_model=MaquinariaResponse
)

def create_maquinaria(

    data: MaquinariaCreate,

    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(

        Product.id == data.id_producto

    ).first()


    if not product:

        raise HTTPException(

            status_code=404,

            detail="Producto no encontrado"
        )


    existing_maquinaria = db.query(Machinery).filter(

        Machinery.product_id == data.id_producto

    ).first()

    if existing_maquinaria:

        raise HTTPException(

            status_code=400,

            detail="Este producto ya tiene datos de maquinaria"
        )

    # -----------------------------------------------------
    # CREAR MAQUINARIA
    # -----------------------------------------------------

    new_maquinaria = Machinery(

        product_id=data.id_producto,
        tipo=data.tipo,
        marca=data.marca,
        modelo=data.modelo,
        year=data.year,
        estado=data.estado

    )

    # -----------------------------------------------------
    # GUARDAR EN DB
    # -----------------------------------------------------

    db.add(new_maquinaria)

    db.commit()

    db.refresh(new_maquinaria)

    # -----------------------------------------------------
    # RESPONSE
    # -----------------------------------------------------

    return MaquinariaResponse(

        id_maquinaria=new_maquinaria.id,

        id_producto=new_maquinaria.product_id,

        tipo=new_maquinaria.tipo,

        marca=new_maquinaria.marca,

        modelo=new_maquinaria.modelo,

        year=new_maquinaria.year,   

        estado=new_maquinaria.estado
    
    )

#=========================================PUT=========================================
@router.put(
    "/{maquinaria_id}",
    response_model=MaquinariaResponse
)

def update_maquinaria(

    maquinaria_id: int,

    data: MaquinariaCreate,

    db: Session = Depends(get_db)
):

    # -----------------------------------------------------
    # BUSCAR MAQUINARIA
    # -----------------------------------------------------

    maquinaria = db.query(Machinery).filter(    
        Machinery.id == maquinaria_id

    ).first()

    # -----------------------------------------------------
    # VALIDAR EXISTENCIA
    # -----------------------------------------------------

    if not maquinaria:

        raise HTTPException(

            status_code=404,

            detail="Maquinaria no encontrada"
        )

    # -----------------------------------------------------
    # ACTUALIZAR DATOS
    # -----------------------------------------------------

    maquinaria.tipo = data.tipo

    maquinaria.marca = data.marca

    maquinaria.modelo = data.modelo

    maquinaria.year = data.year

    maquinaria.estado = data.estado

    # -----------------------------------------------------
    # GUARDAR CAMBIOS
    # -----------------------------------------------------

    db.commit()

    db.refresh(maquinaria)

    # -----------------------------------------------------
    # RESPONSE
    # -----------------------------------------------------

    return MaquinariaResponse(

        id_maquinaria=maquinaria.id,

        id_producto=maquinaria.product_id,

        tipo=maquinaria.tipo,

        marca=maquinaria.marca,

        modelo=maquinaria.modelo,

        year=maquinaria.year,

        estado=maquinaria.estado
    )
#=========================================GET=========================================
@router.get("/",response_model=List[MaquinariaResponse])
def get_all_maquinarias(
    db: Session = Depends(get_db)
):
    maquinarias = db.query(Machinery).all()
    return [MaquinariaResponse.from_orm(maquinaria) for maquinaria in maquinarias]

@router.get(
    "/{maquinaria_id}",response_model=MaquinariaResponse
)
def get_maquinaria_by_id(
    maquinaria_id: int,
    db: Session = Depends(get_db)
):
    maquinaria = db.query(Machinery).filter(Machinery.id == maquinaria_id).first()
    if not maquinaria:
        raise HTTPException(status_code=404, detail="Maquinaria no encontrada")
    return MaquinariaResponse.from_orm(maquinaria)

