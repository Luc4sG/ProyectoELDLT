from pydantic import BaseModel
from typing import List, Dict


    
class CuentaSysacadCreate(BaseModel):
    legajo: str
    password: str
    usuario_id: int

class CuentaSysacadUpdate(BaseModel):
    legajo: str
    password: str
    usuario_id: int

class CuentaCampusCreate(BaseModel):
    username: str
    password: str
    usuario_id: int

class CuentaCampusUpdate(BaseModel):
    username: str
    password: str
    usuario_id: int

    
class ExamenesCreate(BaseModel):
    data: Dict
    usuario_id: int

class ExamenesUpdate(BaseModel):
    data: Dict
    usuario_id: int

class Examenes(BaseModel):
    data: Dict
    id: int
    usuario_id: int
    class Config:
        orm_mode = True


class MateriasActualesCreate(BaseModel):
    nombre_materia: str
    notas: Dict
    inasistencias: int
    usuario_id: int

class MateriasActualesUpdate(BaseModel):
    nombre_materia: str
    notas: Dict
    inasistencias: int
    usuario_id: int

class MateriasActuales(BaseModel):
    id: int
    nombre_materia: str
    notas: Dict
    inasistencias: int
    usuario_id: int
    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nombre: str
    email: str
    
class UsuarioCreate(UsuarioBase):
    password: str
    is_active: bool = True
    
class UsuarioUpdate(BaseModel):
    nombre: str
    email: str
    password: str
    is_active: bool = True
    
class Usuario(UsuarioBase):
    id: int
    is_active: bool = True
    examenes: Examenes 
    materias_actuales: List[MateriasActuales]
    class Config:
        orm_mode = True