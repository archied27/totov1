from fastapi import FastAPI
from app.routes import mpv

app = FastAPI(title="toto backend")

app.include_router(mpv.router, prefix="/mpv", tags=["MPV"])

@app.get("/")
def root():
    return {"message": "Toto backend is running!"}
