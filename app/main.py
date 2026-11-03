from fastapi import FastAPI
from app.core.config import settings
app = FastAPI()

@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "message": settings.PROJECT_NAME}