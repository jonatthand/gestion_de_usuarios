
from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    email:EmailStr
    password:str

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str