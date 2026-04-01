from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models import Task

MONGO_URL = "mongodb+srv://yaswanth:yaswanth12345@cluster1.sxnfzju.mongodb.net/tasks?retryWrites=true&w=majority"

client = AsyncIOMotorClient(MONGO_URL)

async def init_db():
    db = client.get_database("Tasks")   # ✅ force correct DB
    await init_beanie(
        database=db,
        document_models=[Task]
    )
    
    
