from fastapi import FastAPI

from src.routers.booking_proxy import router

app = FastAPI(title="API Gateway")
app.include_router(router)


@app.get("/")
def get_root() -> dict:
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the API Gateway"}


@app.get("/health")
def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}
