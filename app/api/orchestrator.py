from fastapi import APIRouter
router = APIRouter()

@router.get("/status")
async def status():
    return {"head": "ok", "edgesConnected": 0}

@router.post("/self-heal")
async def self_heal():
    # placeholder: enqueue a self-heal job (future)
    return {"triggered": True}

