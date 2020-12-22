from pydantic import BaseModel
from datetime import date

class InicioSesion(BaseModel):
    usuario: str
    contrasena: str

class Register(BaseModel):
    nombre_completo: str
    usuario: str
    fecha_nacimiento: date
    email: str
    tipo_documento: str
    cedula: str
    contrasena: str

class MovimientosIn(BaseModel):
    usuario: str
    fecha: date
    ingreso: str
    egreso: str
    saldo_actual: str

class MovimientosOut(BaseModel):
    usuario: str
    fecha: date
    ingreso: str
    egreso: str
    saldo_actual: str
