from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    name: str
    is_admin: bool = False

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: str
    created_at: datetime
    hashed_password: str

    class Config:
        from_attributes = True
