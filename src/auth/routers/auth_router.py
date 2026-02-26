
# auth/routers/auth_router.py

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.auth.repositories.user_repository import UserRepository    
from src.auth.schemas.user_schema import UserCreateSchema, UserLoginSchema
from src.auth.services.auth_service import AuthService
from src.auth.utils.jwt_handler import get_current_user
from src.core.security import hash_password, verify_password

router = APIRouter(tags=["Auth"])
auth_service = AuthService()

#------------------------------------REGISTRAR CUENTA-------------------------------------------------------------------------------



@router.post("/register")
def register(user_data: UserCreateSchema, db: Session = Depends(get_db)):

    existing_user = UserRepository.get_by_email(db, user_data.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    hashed_pwd = hash_password(user_data.password)

    user = UserRepository.create(db, user_data.email, hashed_pwd)

    return {"message": "Usuario creado correctamente"}

#-------------------------------------LOGUEAR CUENTA------------------------------------------------------------------------------

@router.post("/login")
def login(user_data: UserLoginSchema, db: Session = Depends(get_db)):

    token = auth_service.login_user(db, user_data)

    return {
        "access_token": token,
        "token_type": "bearer"
    }

#-------------------------------------ENDPOINT PROTEGIDO------------------------------------------------------------------------------

@router.get("/me")
def read_current_user(current_user = Depends(get_current_user)):
    return {
        "email": current_user["email"]
    }
