from fastapi import APIRouter, Depends
from config.database import collection_name
from models.model import Todo
from schemas.schemas import todo_serializer, todom_serializer
from bson import ObjectId
from auth.jwt_bearer import jwtBearer



root = APIRouter(
    tags = ["ToDo Operations"]
)


@root.get("/")
async def get_todom():
    to_dos = todom_serializer(collection_name.find())
    return {"status": "OK", "data": to_dos}


@root.get("/{id}")
async def get_todo(id: str):
    to_do =  todom_serializer(collection_name.find({"_id": ObjectId(Id)}))
    return {"status": "OK", "data": to_do}


@root.post("/", dependencies=[Depends(jwtBearer())])
async def post_todo(todo: Todo):
    _id = collection_name.insert_one(dict(todo))
    todo = todom_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "OK", "data": todo}


@root.put("/{id}")
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(todo)
    })
    todo = todom_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "OK", "data": todo}


@root.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "OK", "data": []}
