from fastapi import APIRouter
import datetime

router = APIRouter()

@router.get("/")
async def health():
    return {"status": "ok", "time": datetime.datetime.utcnow().isoformat()}
