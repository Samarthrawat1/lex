from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from db.mongodb import get_db
from schemas.log_entry import LogEntry
from bson import json_util
import json

router = APIRouter()

@router.post("/logs")
async def create_log(log_entry: LogEntry, db: AsyncIOMotorDatabase = Depends(get_db)):
    try:
        log_data = log_entry.model_dump()
        result = await db.logs.insert_one(log_data)
        if not result.inserted_id:
            raise HTTPException(status_code=500, detail="Failed to save log")
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/logs")
async def get_logs(db: AsyncIOMotorDatabase = Depends(get_db)):
    try:
        cursor = db.logs.find({})
        logs = await cursor.to_list(length=None)
        # Convert MongoDB objects to JSON-serializable format
        return json.loads(json_util.dumps(logs))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 