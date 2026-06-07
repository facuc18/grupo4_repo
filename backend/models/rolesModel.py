from sqlalchemy import Column, Integer, String
from database import Base

class Roles (Base):

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)

    nombre = Column(
        String(50),
        nullable=False,
        unique=True
    )