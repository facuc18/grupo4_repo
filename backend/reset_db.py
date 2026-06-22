from database import Base, engine


from models.rolesModel import Roles
from models.usuarioModel import Usuario
from models.categoriaModel import Categoria
from models.publicacionModel import Publicacion
from models.compraModel import Compra
from models.leasingModel import Leasing
from models.cuotaModel import Cuota

#esto es un archivo que se ejecuta en la terminal para reiniciarla(borra toda las tablas y las vuelve a crear esta vez sin datos)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Base reiniciada.")