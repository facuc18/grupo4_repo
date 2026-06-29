from fastapi import FastAPI
from database import Base , engine


#=================== MODELOS ===================
from models.categoriaModel import Categoria
from models.rolesModel import Roles
from models.publicacionModel import Publicacion

#=================== RUTAS ===================
from routes.publicacionRouter import router as publicacion_router
from routes.categoriaRouter import router as categoria_router
from routes.rolesRouter import router as roles_router
from routes.compraRouter import router as compras_router
app = FastAPI()

Base.metadata.create_all(bind=engine)



app.include_router(publicacion_router)
app.include_router(categoria_router)
app.include_router(roles_router)
app.include_router(compras_router)