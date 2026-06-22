from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session

from models.categoriaModel import Categoria
from models.publicacionModel import Publicacion
from models.usuarioModel import Usuario
from database  import get_db

from schemas.publicacionSchema import PublicacionLista,PublicacionDetalle,PublicacionCrear, PublicacionActualizar,PublicacionEliminar

router = APIRouter()

@router.get("/publicaciones", response_model=list[PublicacionLista])
def traer_publicaciones(db:Session = Depends(get_db)):

    resultados = []

    publicaciones = db.query(Publicacion).filter(Publicacion.estado == "ACTIVA").all()

    for publicacion in publicaciones:
        categoria = publicacion.categoria.nombre
  

        resultados.append({
            "id": publicacion.id,
            "titulo": publicacion.titulo,
            "precio": publicacion.precio,
            "categoria": categoria,
        })




    return resultados

@router.get("/publicaciones/{id}",response_model=PublicacionDetalle)
def traer_publicacion_por_id(
    id: int,
    db: Session = Depends(get_db)
):

    publicacion = db.query(Publicacion).filter(Publicacion.id == id).filter(Publicacion.estado == "ACTIVA").first()

    if not publicacion:
        raise HTTPException(
            status_code=404,
            detail="Publicación no encontrada"
        )
 

    categoria = publicacion.categoria
    vendedor = publicacion.vendedor

    return {
        "id": publicacion.id,
        "titulo": publicacion.titulo,
        "descripcion": publicacion.descripcion,
        "precio": publicacion.precio,
        "stock": publicacion.stock,
        "fecha_publicacion": publicacion.fecha_publicacion.isoformat(),

        "categoria": categoria.nombre,

        "vendedor": {
            "id": vendedor.id,
            "nombre": vendedor.nombre
        }
    }

@router.post("/publicaciones",response_model=PublicacionCrear)
def crear_publicacion(publicacion: PublicacionCrear, db: Session = Depends(get_db)):



    nueva_publicacion = Publicacion(
        titulo=publicacion.titulo,
        descripcion=publicacion.descripcion,
        precio=publicacion.precio,
        stock=publicacion.stock,
        categoria_id=publicacion.categoria_id,
        vendedor_id=publicacion.vendedor_id
    )

    db.add(nueva_publicacion)
    db.commit()
    db.refresh(nueva_publicacion)

    return nueva_publicacion

@router.put("/publicaciones/{id}", response_model=PublicacionActualizar)
def actualizar_publicacion(id: int, publicacion: PublicacionActualizar, db: Session = Depends(get_db)):
    publicacion_db = db.query(Publicacion).filter(Publicacion.id == id).first()

    if not publicacion_db:
        raise HTTPException(
            status_code=404,
            detail="Publicación no encontrada"
        )

    for key, value in publicacion.model_dump(exclude_unset=True).items():
        setattr(publicacion_db, key, value)

    db.commit()
    db.refresh(publicacion_db)

    return publicacion_db


@router.delete("/publicaciones/{id}", )
def eliminar_publicacion(id: int, db: Session = Depends(get_db)):
    publicacion_db = db.query(Publicacion).filter(Publicacion.id == id).first()

    if not publicacion_db:
        raise HTTPException(
            status_code=404,
            detail="Publicación no encontrada"
        )

    db.delete(publicacion_db)
    db.commit()

    return {"message": "Publicación eliminada correctamente"}