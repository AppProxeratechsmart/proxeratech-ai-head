from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.orchestrator import router as orch_router

app = FastAPI(title="Proxeratech AI Head")

app.include_router(health_router, prefix="/health")
app.include_router(auth_router, prefix="/api/auth")
app.include_router(orch_router, prefix="/api/orchestrator")

@app.get("/")
async def root():
    return {"service": "proxeratech-head", "status": "ok"}
