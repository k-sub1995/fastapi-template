from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include all V1 routers from api/v1/api.py
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def root():
    """
    Root endpoint for health check.

    Returns:
        dict: Welcome message.
    """
    return {"message": "Welcome to FastAPI template API"}
