from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from jose import JWTError
from src.core.database import get_db
from src.auth.repositories.user_repository import UserRepository
from src.auth.utils.jwt_handler import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


bearer_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = UserRepository.get_by_email(db, email)

    if user is None:
        raise credentials_exception

    return user

