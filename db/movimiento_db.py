from datetime import date
from pydantic import BaseModel
from typing import Dict

class MovimientosInDB(BaseModel):
    id_movimiento: int = 0
    usuario: str
    fecha: date
    ingreso: int
    egreso: int
    saldo_actual:int

database_movimientos = []
generator = {"id":0}

#llama al usuario si existe, y retorna los datos
def save_movimiento(movimiento_in_db: MovimientosInDB):
    generator["id"] = generator["id"] + 1
    movimiento_in_db.id_movimiento = generator["id"]
    database_movimientos.append(movimiento_in_db)
    return movimiento_in_db

def get_movimiento(codigo_movimiento: str):
    if codigo_movimiento in database_movimientos:
        return database_movimientos[codigo_movimiento]
    else:
        return None

        