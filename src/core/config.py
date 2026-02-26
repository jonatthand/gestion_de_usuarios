from datetime import timedelta

SECRET_KEY = "super-secret-key-change-this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_token_expiration():
    return timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)