
# auth/routers/auth_router.py

from fastapi import APIRouter, status
from auth.schemas.user_schema import UserCreateSchema
from auth.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

@router.post("/cuenta", status_code=status.HTTP_201_CREATED)
def crear_cuenta(user_data: UserCreateSchema):
    resultado = auth_service.registrar_usuario(user_data)

    return {
        "message": "Cuenta creada exitosamente"
    }


#-------------------------------------------------------------------------------------------------------------------



app.post('/registro', tags=['Registro de usuario'])
def registrar_usuario(username: str, password: str):
    datos = request.body() # email, password son los datos que vienen del request
    #request.body() son los datos que vienen del request almacenados en la variable datos
    #el request viene del controlador o router (acá)

    resultado = auth_service.registrar_usuario(datos)
    #resultado es la variable que almacena la respuesta del servicio
    #auth_service es la capa de servicio que maneja la lógica de negocio
    #registrar_usuario es la función del servicio que maneja el registro de usuario
    #(datos) son los datos que se envían al servicio para procesar el registro
    
    #la informacion de los datos viene del controlador y se envia al servicio
    # Colocar en que capa se realiza cada validación (servicio, controlador, repositorio)
    # con el schema de pydantic se validan los datos en el controlador

    if resultado['exito']:
        # Se devuelve un mensaje de éxito si el registro fue exitoso
    else:
        # Se devuelve un mensaje de error si hubo algún problema durante el registro

    #se hace la condicion dependiendo del resultado del servicio
    return {'message': 'Usuario registrado exitosamente'}