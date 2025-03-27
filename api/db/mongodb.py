from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client[settings.MONGODB_DB_NAME]

async def get_db():
    """
    Get database instance.
    """
    try:
        await client.admin.command('ping')  # Test the connection
        return database
    except Exception as e:
        print(f"Database connection error: {e}")  # Debug print
        return None

async def connect_to_mongo():
    """
    Connect to MongoDB.
    """
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    database = client[settings.MONGODB_DB_NAME]

async def close_mongo_connection():
    """
    Close MongoDB connection.
    """
    if client:
        client.close() 