from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from src.auth.repositories.user_repository import UserRepository 
from src.core.config import SECRET_KEY, ALGORITHM, get_token_expiration


ACCESS_TOKEN_EXPIRE_MINUTES = 60
bearer_scheme = HTTPBearer()

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + get_token_expiration()
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise

#---------------------LIBRERIA PARA LOS ENDPOINTS PROTEGIDOS-------------------------------------------------------------------

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):

    token = credentials.credentials

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = UserRepository.get_by_email(db, email)

    if user is None:
        raise credentials_exception

    return user

