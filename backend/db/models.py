# USUARIO >> ID NOMBRE EMAIL CONTRASEÑA CUENTASYSACAD-FK CUENTACAMPUS-FK
#     CUENTASYSACAD >> ID USUARIO-FK LEGAJO PASSWORD
#     CUENTACAMPUS >> ID USUARIO-FK USERNAME PASSWORD
#     ------SYSACAD------
#     EXAMENES >> ID USUARIO-FK DATA.JSON
#     MATERIAS_ACTUALES >> ID NOMBRE-MATERIA USUARIO-FK NOTAS.JSON INASISTENCIAS
#     ------CAMPUS------
#     TODO: definir que le ponemos al campus y que necesitamos del mismo


from sqlalchemy import Column, Integer, String, ForeignKey, JSON, PrimaryKeyConstraint, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship
# from datetime import datetime
import sys

sys.path.append('..')
from db.databse import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    cuentasysacad = relationship("CuentaSysacad", back_populates="usuario")
    cuentacampus = relationship("CuentaCampus", back_populates="usuario")
    examenes = relationship("Examenes", back_populates="usuario")
    materias_actuales = relationship("MateriasActuales", back_populates="usuario")
    

class CuentaSysacad(Base):
    __tablename__ = 'cuentasysacad'
    id = Column(Integer, primary_key=True, index=True)
    legajo = Column(String, nullable=False)
    password = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False, unique=True)

    usuario = relationship("Usuario", back_populates="cuentasysacad")

class Examenes(Base):
    __tablename__ = 'examenes'
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="examenes")

class MateriasActuales(Base):
    __tablename__ = 'materias_actuales'
    id = Column(Integer, primary_key=True, index=True)
    nombre_materia = Column(String, nullable=False)
    notas = Column(JSON, nullable=False)
    inasistencias = Column(Integer, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="materias_actuales")

class CuentaCampus(Base):
    __tablename__ = 'cuentacampus'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False, unique=True)

    usuario = relationship("Usuario", back_populates="cuentacampus")