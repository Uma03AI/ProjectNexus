import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("ProjectNexus")

client = AsyncIOMotorClient(MONGO_URL)
database = client["ProjectNexus"]

# Example collection
users_collection = database.get_collection("users")
