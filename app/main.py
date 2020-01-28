from fastapi import FastAPI
from app.services.database import database
from app.services.logger import logger

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

@app.get("/")
def read_root():
    logger.debug("GET /");
    return {"status": "OK"}
