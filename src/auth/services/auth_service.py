
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.auth.schemas.user_schema import UserCreateSchema 
from src.auth.repositories.user_repository import UserRepository 
from passlib.context import CryptContext
from src.auth.utils.jwt_handler import create_access_token
from src.core.security import verify_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#---------------------------------------CREAR CUENTA------------------------------------------------------------

class AuthService:

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def register_user(self, user_data: UserCreateSchema):
        # Verificar si el usuario ya existe
        existing_user = UserRepository.get_by_email(user_data.email)
        if existing_user:
            raise ValueError("El usuario ya existe")

        # Hashear contraseña
        hashed_password = self.hash_password(user_data.password)

        # Guardar usuario
        user = UserRepository.create(
            email=user_data.email,
            hashed_password=hashed_password
        )

        return user

    def login_user(self, db: Session, user_data):

        # 1️⃣ Buscar usuario en DB
        user = UserRepository.get_by_email(db, user_data.email)

        if not user:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        # 2️⃣ Verificar contraseña
        if not verify_password(user_data.password, user.password):
            raise HTTPException(status_code=401, detail="Credenciales inválidass")

        # 3️⃣ Crear token
        token = create_access_token({"sub": user.email})

        return token

#--------------------------------------LOGIN-------------------------------------------------------------


    #------------------------------------------------------------------------------