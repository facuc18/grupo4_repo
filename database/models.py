# database/models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    Enum as SQLEnum,
    Text
)

from sqlalchemy.orm import declarative_base, relationship

from datetime import datetime, UTC
import enum


Base = declarative_base()


# =========================================================
# ENUMS
# =========================================================

class UserType(str, enum.Enum):
    PERSON = "persona_fisica"
    COMPANY = "empresa"


class EspecieEnum(str, enum.Enum):
    CATTLE = "vacuno"
    SHEEP = "ovino"
    PIG = "porcino"
    BIRD = "aves"
    HORSE = "equino"


class EstadoMaquinariaEnum(str, enum.Enum):
    NUEVA = "nueva"
    USADA = "usada"
    REPARACION = "en_reparacion"


class TipoMaquinariaEnum(str, enum.Enum):
    TRACTOR = "tractor"
    COSECHADORA = "cosechadora"
    SEMBRADORA = "sembradora"
    PULVERIZADORA = "pulverizadora"
    ENFARDADORA = "enfardadora"
    TOLVA = "tolva"
    ARADO = "arado"
    RASTRA = "rastra"
    FERTILIZADORA = "fertilizadora"
    MIXER = "mixer"

class tipo_publicacionEnum(str, enum.Enum):
    VENTA = "venta"
    LEASING = "leasing"


class LeaseStatus(str, enum.Enum):
    PENDING = "pendiente"
    APPROVED = "aprobado"
    REJECTED = "rechazado"
    ACTIVE = "activo"
    COMPLETED = "completado"


class PaymentStatus(str, enum.Enum):
    PENDING = "pendiente"
    COMPLETED = "completado"
    FAILED = "fallido"


class ReportStatus(str, enum.Enum):
    PENDING = "pendiente"
    REVIEWED = "revisado"
    RESOLVED = "resuelto"


# =========================================================
# USERS
# =========================================================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    user_type = Column(
        SQLEnum(UserType),
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    document_id = Column(
        String(50),
        unique=True
    )

    phone = Column(String(20))

    address = Column(Text)

    is_active = Column(
        Boolean,
        default=True
    )

    is_blocked = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    # RELATIONSHIPS

    products = relationship(
        "Product",
        back_populates="seller",
        cascade="all, delete"
    )

    purchases = relationship(
        "Purchase",
        back_populates="buyer"
    )

    lease_requests_sent = relationship(
        "Lease",
        foreign_keys="Lease.buyer_id",
        back_populates="buyer"
    )

    lease_requests_received = relationship(
        "Lease",
        foreign_keys="Lease.seller_id",
        back_populates="seller"
    )


# =========================================================
# PRODUCTS
# =========================================================

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    seller_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    description = Column(Text)

    price = Column(
        Float,
        nullable=False
    )

    stock = Column(
        Integer,
        default=1
    )

    is_available = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )

    # RELATIONSHIPS

    seller = relationship(
        "User",
        back_populates="products"
    )

    images = relationship(
        "ProductImage",
        back_populates="product",
        cascade="all, delete"
    )

    purchases = relationship(
        "PurchaseItem",
        back_populates="product"
    )

    leases = relationship(
        "Lease",
        back_populates="product"
    )

    animal = relationship(
        "Animal",
        back_populates="product",
        uselist=False,
        cascade="all, delete"
    )

    machinery = relationship(
        "Machinery",
        back_populates="product",
        uselist=False,
        cascade="all, delete"
    )


# =========================================================
# ANIMALS
# =========================================================

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
        unique=True
    )

    especie = Column(
        SQLEnum(EspecieEnum),
        nullable=False
    )

    raza = Column(String(100))

    edad = Column(Integer)

    peso = Column(Float)

    product = relationship(
        "Product",
        back_populates="animal"
    )


# =========================================================
# MACHINERY
# =========================================================

class Machinery(Base):
    __tablename__ = "machineries"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
        unique=True
    )

    tipo = Column(
        SQLEnum(TipoMaquinariaEnum),
        nullable=False
    )

    marca = Column(String(100))

    modelo = Column(String(100))

    anio = Column(Integer)

    estado = Column(
        SQLEnum(EstadoMaquinariaEnum),
        nullable=False
    )

    product = relationship(
        "Product",
        back_populates="machinery"
    )


# =========================================================
# PRODUCT IMAGES
# =========================================================

class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    image_url = Column(
        String(500),
        nullable=False
    )

    is_main = Column(
        Boolean,
        default=False
    )

    product = relationship(
        "Product",
        back_populates="images"
    )


# =========================================================
# PURCHASES
# =========================================================

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)

    buyer_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    purchase_date = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    total_amount = Column(
        Float,
        nullable=False
    )

    payment_status = Column(
        SQLEnum(PaymentStatus),
        default=PaymentStatus.PENDING
    )

    payment_method = Column(String(50))

    transaction_id = Column(String(255))

    buyer = relationship(
        "User",
        back_populates="purchases"
    )

    items = relationship(
        "PurchaseItem",
        back_populates="purchase",
        cascade="all, delete"
    )


# =========================================================
# PURCHASE ITEMS
# =========================================================

class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id = Column(Integer, primary_key=True, index=True)

    purchase_id = Column(
        Integer,
        ForeignKey("purchases.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        default=1
    )

    unit_price = Column(
        Float,
        nullable=False
    )

    purchase = relationship(
        "Purchase",
        back_populates="items"
    )

    product = relationship(
        "Product",
        back_populates="purchases"
    )


# =========================================================
# LEASING
# =========================================================

class Lease(Base):
    __tablename__ = "leases"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    buyer_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    seller_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    total_amount = Column(
        Float,
        nullable=False
    )

    installment_count = Column(
        Integer,
        nullable=False
    )

    installment_value = Column(
        Float,
        nullable=False
    )

    status = Column(
        SQLEnum(LeaseStatus),
        default=LeaseStatus.PENDING
    )

    request_date = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    approved_date = Column(DateTime)

    product = relationship(
        "Product",
        back_populates="leases"
    )

    buyer = relationship(
        "User",
        foreign_keys=[buyer_id],
        back_populates="lease_requests_sent"
    )

    seller = relationship(
        "User",
        foreign_keys=[seller_id],
        back_populates="lease_requests_received"
    )

    payments = relationship(
        "LeasePayment",
        back_populates="lease",
        cascade="all, delete"
    )


# =========================================================
# LEASE PAYMENTS
# =========================================================

class LeasePayment(Base):
    __tablename__ = "lease_payments"

    id = Column(Integer, primary_key=True, index=True)

    lease_id = Column(
        Integer,
        ForeignKey("leases.id"),
        nullable=False
    )

    installment_number = Column(
        Integer,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    due_date = Column(
        DateTime,
        nullable=False
    )

    payment_date = Column(DateTime)

    is_paid = Column(
        Boolean,
        default=False
    )

    transaction_id = Column(String(255))

    lease = relationship(
        "Lease",
        back_populates="payments"
    )


# =========================================================
# BLOCKED IPS
# =========================================================

class BlockedIP(Base):
    __tablename__ = "blocked_ips"

    id = Column(Integer, primary_key=True, index=True)

    ip_address = Column(
        String(45),
        unique=True,
        nullable=False
    )

    reason = Column(Text)

    blocked_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    blocked_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )


# =========================================================
# REPORTS
# =========================================================

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    reporter_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    reported_user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    reported_product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    reason = Column(
        Text,
        nullable=False
    )

    status = Column(
        SQLEnum(ReportStatus),
        default=ReportStatus.PENDING
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    resolved_at = Column(DateTime)