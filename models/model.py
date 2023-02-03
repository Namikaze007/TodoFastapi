from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class Todo(BaseModel):
    name: str
    description: str
    completed: bool
    # date: datetime.date


class User(BaseModel):
    fname: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

