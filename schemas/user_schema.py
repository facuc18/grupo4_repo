from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum


# =========================
# ENUMS
# =========================

class UserTypeEnum(str, Enum):
    PERSON = "persona_fisica"
    COMPANY = "empresa"


# =========================
# BASE
# =========================
# Campos comunes que comparten varios schemas

class UserBase(BaseModel):
    email: EmailStr
    name: str
    user_type: UserTypeEnum
    phone: Optional[str] = None
    document_id: Optional[str] = None


# =========================
# CREATE
# =========================
# Datos necesarios para crear un usuario

class UserCreate(UserBase):
    password: str


# =========================
# UPDATE
# =========================
# Campos opcionales para actualizar usuario

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


# =========================
# RESPONSE
# =========================
# Datos que devuelve la API

class UserResponse(UserBase):
    id: int
    is_active: bool
    is_blocked: bool
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# LOGIN
# =========================
# Datos para iniciar sesión

class UserLogin(BaseModel):
    email: EmailStr
    password: str


# =========================
# TOKEN RESPONSE
# =========================
# Respuesta del login JWT

class TokenResponse(BaseModel):
    access_token: str
    token_type: str