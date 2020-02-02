# app.main

from fastapi import FastAPI
from .services.database import database
from .services.logger import logger
from .routers import root, users

app = FastAPI(
    title="FastAPI-Proj",
    description="Base project",
    version="1.0.0",
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(root.router)
app.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)
