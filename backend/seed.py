from database import SessionLocal

from models.rolesModel import Roles
from models.usuarioModel import Usuario
from models.categoriaModel import Categoria
from models.publicacionModel import Publicacion
#estos son datos de prueba ,lo ejecutas en la base de datos y ya te mete datos de prueba a la base de datos


db = SessionLocal()

# =========================
# ROLES
# =========================

admin = Roles(nombre="ADMIN")
vendedor = Roles(nombre="VENDEDOR")
comprador = Roles(nombre="COMPRADOR")

db.add_all([
    admin,
    vendedor,
    comprador
])

db.commit()

# =========================
# CATEGORIAS
# =========================

ganado = Categoria(
    nombre="Ganado Vacuno",
    descripcion="Compra y venta de ganado"
)

tractores = Categoria(
    nombre="Tractores",
    descripcion="Maquinaria agrícola"
)

sembradoras = Categoria(
    nombre="Sembradoras",
    descripcion="Equipos de siembra"
)

db.add_all([
    ganado,
    tractores,
    sembradoras
])

db.commit()

# =========================
# USUARIOS
# =========================

juan = Usuario(
    nombre="Juan Perez",
    email="juan@gmail.com",
    password_hash="123456",
    telefono="2314555555",
    rol_id=vendedor.id
)

pedro = Usuario(
    nombre="Pedro Gomez",
    email="pedro@gmail.com",
    password_hash="123456",
    telefono="2314666666",
    rol_id=vendedor.id
)

administrador = Usuario(
    nombre="Administrador",
    email="admin@gmail.com",
    password_hash="123456",
    telefono="2314777777",
    rol_id=admin.id
)

db.add_all([
    juan,
    pedro,
    administrador
])

db.commit()

# =========================
# PUBLICACIONES
# =========================

p1 = Publicacion(
    titulo="Tractor John Deere 7815",
    descripcion="Tractor en excelente estado",
    precio=50000,
    stock=1,
    categoria_id=tractores.id,
    vendedor_id=juan.id
)

p2 = Publicacion(
    titulo="Tractor Massey Ferguson",
    descripcion="Motor recién reparado",
    precio=45000,
    stock=1,
    categoria_id=tractores.id,
    vendedor_id=juan.id
)

p3 = Publicacion(
    titulo="Lote de 20 vacas Angus",
    descripcion="Ganado certificado",
    precio=25000,
    stock=20,
    categoria_id=ganado.id,
    vendedor_id=pedro.id
)

p4 = Publicacion(
    titulo="Toro reproductor",
    descripcion="Excelente genética",
    precio=8000,
    stock=1,
    estado="INACTIVA",
    categoria_id=ganado.id,
    vendedor_id=pedro.id
)

p5 = Publicacion(
    titulo="Sembradora Agrometal TX",
    descripcion="Sembradora usada en muy buen estado",
    precio=38000,
    stock=1,
    categoria_id=sembradoras.id,
    vendedor_id=juan.id
)

db.add_all([
    p1,
    p2,
    p3,
    p4,
    p5
])

db.commit()

print("Seed ejecutado correctamente")