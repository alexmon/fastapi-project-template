from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.get("/")
async def read_users(token: str = Depends(oauth2_scheme)):
    return {"token": token}

