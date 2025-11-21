from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt
from passlib.context import CryptContext
import os

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginIn(BaseModel):
    username: str
    password: str

# demo user (replace with DB in future)
_demo_user = {"username": "admin", "password_hash": pwd_context.hash("password")}

@router.post("/login")
async def login(payload: LoginIn):
    if payload.username != _demo_user["username"] or not pwd_context.verify(payload.password, _demo_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": payload.username}, os.environ.get("JWT_SECRET", "devsecret"), algorithm="HS256")
    return {"access_token": token}
