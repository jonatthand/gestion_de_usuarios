
from pydantic import BaseModel, EmailStr, Field
#pydantic es una librería que permite la validación de datos y la creación de modelos de datos en Python
#BaseModel es la clase base para crear modelos de datos
#EmailStr es un tipo de dato que valida que el valor sea un correo electrónico válido
#Field se utiliza para agregar metadatos y validaciones adicionales a los campos del modelo


class UserCreateSchema(BaseModel):
    email:EmailStr
    password:str

