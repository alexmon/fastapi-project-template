# app.routers.users

from fastapi import APIRouter, Depends
from app.security import oauth2_scheme

router = APIRouter()

@router.get("/")
async def read_users(token: str = Depends(oauth2_scheme)):
    return {"token": token}

