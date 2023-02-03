from fastapi import FastAPI
from routes.route import root
from routes.users import router
from auth.jwt_handler import signJWT

app = FastAPI()

@app.get("/")
def get_start():
    return {"Hello": "Wobot"}


app.include_router(root)
app.include_router(router)
