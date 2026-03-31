from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from schema import Task

employees = [
    {"id": 1, "name": "Alice", "age": 30, "position": "Software Engineer", "salary": 80000},
    {"id": 2, "name": "Bob", "age": 35, "position": "Project Manager", "salary": 90000},
    {"id": 3, "name": "Charlie", "age": 28, "position": "Data Scientist", "salary": 95000}
]


MONGO_URL = "mongodb+srv://yaswanth:12345@cluster1.sxnfzju.mongodb.net/tasks?retryWrites=true&w=majority"

client = AsyncIOMotorClient(MONGO_URL)

async def init_db():
    db = client.get_database("Tasks")   # ✅ force correct DB
    
    print(type(db))  # debug

    await init_beanie(
        database=db,
        document_models=[Task]
    )