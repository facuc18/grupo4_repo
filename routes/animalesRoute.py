from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database.config import get_db

from database.models import (
    Product,
    Animal
)

from schemas.animal_schema import (
    AnimalCreate,
    AnimalResponse
)

router = APIRouter(
    prefix="/animals",
    tags=["Animals"]
)

#==========================================POST=========================================
@router.post(
    "/",
    response_model=AnimalResponse
)

def create_animal(

    data: AnimalCreate,

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


    existing_animal = db.query(Animal).filter(

        Animal.product_id == data.id_producto

    ).first()

    if existing_animal:

        raise HTTPException(

            status_code=400,

            detail="Este producto ya tiene datos de animal"
        )

    # -----------------------------------------------------
    # CREAR ANIMAL
    # -----------------------------------------------------

    new_animal = Animal(

        product_id=data.id_producto,

        especie=data.especie,

        raza=data.raza,

        peso=data.peso,

        edad=data.edad
    )

    # -----------------------------------------------------
    # GUARDAR EN DB
    # -----------------------------------------------------

    db.add(new_animal)

    db.commit()

    db.refresh(new_animal)

    # -----------------------------------------------------
    # RESPONSE
    # -----------------------------------------------------

    return AnimalResponse(

        id_animal=new_animal.id,

        id_producto=new_animal.product_id,

        especie=new_animal.especie,

        raza=new_animal.raza,

        peso=new_animal.peso,

        edad=new_animal.edad
    )

#=========================================PUT=========================================
@router.put(
    "/{animal_id}",
    response_model=AnimalResponse
)

def update_animal(

    animal_id: int,

    data: AnimalCreate,

    db: Session = Depends(get_db)
):

    # -----------------------------------------------------
    # BUSCAR ANIMAL
    # -----------------------------------------------------

    animal = db.query(Animal).filter(

        Animal.id == animal_id

    ).first()

    # -----------------------------------------------------
    # VALIDAR EXISTENCIA
    # -----------------------------------------------------

    if not animal:

        raise HTTPException(

            status_code=404,

            detail="Animal no encontrado"
        )

    # -----------------------------------------------------
    # ACTUALIZAR DATOS
    # -----------------------------------------------------

    animal.especie = data.especie

    animal.raza = data.raza

    animal.peso = data.peso

    animal.edad = data.edad

    # -----------------------------------------------------
    # GUARDAR CAMBIOS
    # -----------------------------------------------------

    db.commit()

    db.refresh(animal)

    # -----------------------------------------------------
    # RESPONSE
    # -----------------------------------------------------

    return AnimalResponse(

        id_animal=animal.id,

        id_producto=animal.product_id,

        especie=animal.especie,

        raza=animal.raza,

        peso=animal.peso,

        edad=animal.edad
    )
#=========================================GET=========================================
@router.get("/",response_model=List[AnimalResponse])
def get_all_animals(
    db: Session = Depends(get_db)
):
    animals = db.query(Animal).all()
    return [AnimalResponse.from_orm(animal) for animal in animals]

@router.get(
    "/{animal_id}",response_model=AnimalResponse
)
def get_animal_by_id(
    animal_id: int,
    db: Session = Depends(get_db)
):
    animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return AnimalResponse.from_orm(animal)

