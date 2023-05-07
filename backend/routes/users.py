from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import sys

sys.path.append("..")
from util import schemas, deps
from crud import crud_usuarios

router = APIRouter()

@router.post("/usuarios/", response_model=schemas.Usuario)
async def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(deps.get_db)):
    data=crud_usuarios.get_usuarios_email(usuario.email, db)
    if data is not None:
        return JSONResponse(status_code=400, content={"message": "El usuario ya existe"})
    data=crud_usuarios.create_usuario(usuario, db)
    if data is None:
        return JSONResponse(status_code=400, content={"message": "Error creando usuario"})
    return JSONResponse(status_code=200, content={"message": "Usuario creado exitosamente"})

@router.get("/usuarios/", response_model=schemas.Usuario)
async def get_all_usuario(db: Session = Depends(deps.get_db)):
    data=crud_usuarios.get_all_usuario(db)
    if data is None:
        return JSONResponse(status_code=400, content={"message": "Error obteniendo usuarios"})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@router.delete("/{user_id}", response_model=schemas.Usuario)
async def delete_user(user_id: int, db: Session = Depends(deps.get_db)) -> JSONResponse:
    """ Delete A User"""
    data = crud_usuarios.delete_usuario(usuario_id=user_id, db=db)
    if data is None:
        return JSONResponse(status_code=500,
                            content={"message": "Internal Server Error"})
    return JSONResponse(status_code=200,
                        content={"message": "success"})

@router.put("/{user_id}", response_model=schemas.Usuario)
async def update_user(user_id: int, user: schemas.UsuarioUpdate,
                db: Session = Depends(deps.get_db)) -> JSONResponse:
    """ Update A User"""

    data = crud_usuarios.update_usuario(usuario_id=user_id, usuario=user, db=db)
    if data is None:
        return JSONResponse(status_code=500,
                            content={"message": "Internal Server Error"})
    return JSONResponse(status_code=200,
                        content={"message": "success"})