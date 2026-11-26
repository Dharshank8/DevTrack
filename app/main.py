
from fastapi import FastAPI

app = FastAPI(
    title="DevTrack API",
    description="Project and Issue Management System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to DevTrack API",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "application": "DevTrack"
    }
