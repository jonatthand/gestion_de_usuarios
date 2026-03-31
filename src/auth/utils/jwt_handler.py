from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from src.core.config import SECRET_KEY, ALGORITHM, get_token_expiration

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

