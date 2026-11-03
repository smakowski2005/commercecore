from fastapi import FastAPI
from app.core.config import settings
from app.api.users import router as users_router

app = FastAPI()

app.include_router(users_router)
@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "message": settings.PROJECT_NAME}