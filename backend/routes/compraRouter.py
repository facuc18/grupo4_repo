
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db

from models.compra import Compra
from models.publicacion import Publicacion

from schemas.compra import (
    CompraCreate,
    CompraResponse,
    CompraEstadoUpdate
)

router = APIRouter(
    prefix="/compras",
    tags=["Compras"]
)
@router.post(
    "/",
    response_model=CompraResponse,
    status_code=status.HTTP_201_CREATED
)
def crear_compra(
    compra: CompraCreate,
    db: Session = Depends(get_db)
):

    publicacion = (
        db.query(Publicacion)
        .filter(Publicacion.id == compra.publicacion_id)
        .first()
    )

    if not publicacion:
        raise HTTPException(
            status_code=404,
            detail="Publicación no encontrada"
        )

    nueva_compra = Compra(
        monto_total=publicacion.precio,
        estado_pago="pendiente",
        comprador_id=1,  # temporal
        publicacion_id=publicacion.id
    )

    db.add(nueva_compra)
    db.commit()
    db.refresh(nueva_compra)

    return nueva_compra
@router.get(
    "/",
    response_model=list[CompraResponse]
)
def listar_compras(
    db: Session = Depends(get_db)
):

    compras = db.query(Compra).all()

    return compras
@router.get(
    "/{compra_id}",
    response_model=CompraResponse
)
def obtener_compra(
    compra_id: int,
    db: Session = Depends(get_db)
):

    compra = (
        db.query(Compra)
        .filter(Compra.id == compra_id)
        .first()
    )

    if not compra:
        raise HTTPException(
            status_code=404,
            detail="Compra no encontrada"
        )

    return compra
@router.patch(
    "/{compra_id}",
    response_model=CompraResponse
)
def actualizar_estado_pago(
    compra_id: int,
    datos: CompraEstadoUpdate,
    db: Session = Depends(get_db)
):

    compra = (
        db.query(Compra)
        .filter(Compra.id == compra_id)
        .first()
    )

    if not compra:
        raise HTTPException(
            status_code=404,
            detail="Compra no encontrada"
        )

    compra.estado_pago = datos.estado_pago

    db.commit()
    db.refresh(compra)

    return compra
@router.delete(
    "/{compra_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_compra(
    compra_id: int,
    db: Session = Depends(get_db)
):

    compra = (
        db.query(Compra)
        .filter(Compra.id == compra_id)
        .first()
    )

    if not compra:
        raise HTTPException(
            status_code=404,
            detail="Compra no encontrada"
        )

    db.delete(compra)
    db.commit()