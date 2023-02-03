from fastapi import APIRouter, Body
from models.model import User, UserLogin
from auth.jwt_handler import signJWT

router = APIRouter(
    tags = ["User Routes"]
)

users = []

@router.get("/")
def get():
    return {"Hello": "Wob"}


@router.post("/user/signup")
def user_signup(user: User = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLogin):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


@router.post("/user/login")
def user_login(user: UserLogin = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error": "Invalid login details"
        }
