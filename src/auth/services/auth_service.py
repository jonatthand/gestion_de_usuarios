

from auth.schemas.user_schema import UserCreateSchema #importa el esquema de usuario para la creación de usuarios
from auth.repositories.user_repository import UserRepository #importa el repositorio de usuarios para interactuar con la base de datos
from auth.securirty.password_hasher import PasswordHasher #importa la clase para hashear contraseñas

class AuthService: #Servicio de autenticación que maneja la lógica de negocio relacionada con usuarios

    def __init__(self): #Inicializa las dependencias del servicio
        #__init__ es el constructor de la clase
        #self significa que es un atributo de la clase
        self.user_repository = UserRepository() #Repositorio para operaciones de usuario
        self.password_hasher = PasswordHasher() #Clase para hashear contraseñas


    def registrar_usuario(self, user_data: UserCreateSchema): #Registra un nuevo usuario en el sistema
        # 1. Verificar si el mail ya existe (repositorio)
        # 2. Valirdar reglas de negocio de la contraseña (servicio)
        # 3. Hashear la contraseña (servicio)
        # 4. Crear el usuario en la base de datos (repositorio)
        # 5. Manejar errores y retornar resultados apropiados (servicio)
        pass
        #pass se usa para indicar que no hay implementación aún

