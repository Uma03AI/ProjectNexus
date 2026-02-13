from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import users_collection
from bson import ObjectId
from fastapi import Form

app = FastAPI()

# Enable CORS (optional but recommended)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")


# Root route - serve frontend
@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")

@app.get("/ai/")
async def serve_ai():
    return FileResponse("static/ai.html")

@app.get("/interview-chatbot/")
async def serve_interview():
    return FileResponse("static/interview-chatbot.html")


# Create user
@app.post("/users/")
async def create_user(
    email: str = Form(...),
    skill: str = Form(...)
):
    user = {
        "email": email,
        "skill": skill
    }

    result = await users_collection.insert_one(user)

    return {"message": "User created successfully 🚀"}


# Get all users
@app.get("/users/")
async def get_users():
    users = []
    async for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users