'''
app.routers.auth
'''

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user import get_by_username

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    existing_user = get_by_username(form_data.username)
    if not existing_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not existing_user.match_password(form_data.password, existing_user.salt, existing_user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": existing_user.username, "token_type": "bearer"}

