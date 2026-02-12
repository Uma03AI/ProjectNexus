from fastapi import FastAPI
from database import users_collection
from bson import ObjectId

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "MongoDB connected successfully 🚀"}


@app.post("/users/")
async def create_user(user: dict):
    result = await users_collection.insert_one(user)
    return {"id": str(result.inserted_id)}


@app.get("/users/")
async def get_users():
    users = []
    async for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users
