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