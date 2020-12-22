from db.registro_usuario_db import usuarioDB
from db.registro_usuario_db import update_usuario, get_usuario
#from db.movimiento_db import MovimientosInDB, save_movimiento, get_movimiento
from models.usuarios_models import InicioSesion, Register, MovimientosIn, MovimientosOut

import datetime
from fastapi import FastAPI, HTTPException
from datetime import date

api = FastAPI()

#########################################################
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "http://localhost:8081", 
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
#########################################################

@api.post("/user/auth/")
async def auth_user(user_in: InicioSesion):

    nuevo_usuario = get_usuario(user_in.usuario)

    if nuevo_usuario == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if nuevo_usuario.contrasena != user_in.contrasena:
        return  {"Autenticado": False}

    return  {"Autenticado": True}



@api.get("/user/historial/{usuario}")
async def get_user(usuario: str):

    nuevo_usuario = get_usuario(usuario)

    if nuevo_usuario == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = Register(**nuevo_usuario.dict())

    return  user_out

@api.get("/user/movimientos/{usuario}")
async def get_mov(usuario: str):
    
    validacion = get_usuario(usuario)
    
    if validacion == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    mov_out = MovimientosIn(**validacion.dict())
    return  mov_out
