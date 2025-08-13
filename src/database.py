import os
from pymongo import ASCENDING
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DB]

# Colección de tareas
tasks_collection = db["tasks"]


async def init_db():
    await tasks_collection.create_index([("title", ASCENDING)], unique=True)
