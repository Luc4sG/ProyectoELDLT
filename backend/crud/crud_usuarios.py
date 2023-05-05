from sqlalchemy.orm import Session 
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import defer
from typing import Any
import sys

sys.path.append("..")
from db import models
from util import schemas, passutil

#CRUD de usuarios
class CRUDUsuarios:
    def create_usuario(self, user: schemas.UsuarioCreate, db: Session) -> Any:
    #Agregar un usuario
        try:
            hasshed_password = passutil.get_password_hash(user.password)
            db_user = models.Usuario(nombre=user.nombre,
                                    email=user.email,
                                    password=hasshed_password,
                                    is_active=user.is_active)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e: 
            print("Error creando usuario: ", e)
            return None
        
    def get_usuario_id(self, usuario_id: int, db: Session) -> Any:
    #Obtener un usuario por id
        try:
            return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
        except SQLAlchemyError as e: 
            print("Error obteniendo usuario: ", e)
            return None
        
    def get_usuarios_email(self, email: str, db: Session) -> Any:
    #Obtener un usuario por email
        try:
            return db.query(models.Usuario).filter(models.Usuario.email == email).first()
        except SQLAlchemyError as e: 
            print("Error obteniendo usuario: ", e)
            return None
        
    def get_all_usuario(self,  db: Session) -> Any:
    #Obtener todos los usuarios
        try:
            return db.query(models.Usuario).options(defer('password')).all()
        except SQLAlchemyError as e: 
            print("Error obteniendo usuarios: ", e)
            return None
        
    def update_usuario(self, usuario_id: int, usuario: schemas.UsuarioUpdate, db: Session) -> Any:
    #Se actualiza un usuario
        try: 
            db_user = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

            db_user.nombre = usuario.nombre
            db_user.email = usuario.email
            db_user.password = passutil.get_password_hash(usuario.password)
            db_user.is_active = usuario.is_active

            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            print("Error actualizando usuario: ", e)
            return None
        
    def delete_usuario(self, usuario_id: int, db: Session) -> Any:
    #Se elimina un usuario
        try:
            db_user = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
            db.delete(db_user)
            db.commit()
            return True
        except SQLAlchemyError as e:
            print("Error eliminando usuario: ", e)
            return None
        


crud_usuarios = CRUDUsuarios()
