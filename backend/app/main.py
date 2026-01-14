from fastapi import FastAPI
from app.routes import mpv, dolphin

app = FastAPI(title="toto backend")

app.include_router(mpv.router, prefix="/mpv", tags=["MPV"])
app.include_router(dolphin.router, prefix="/dolphin", tags=["DOLPHIN"])

@app.get("/")
def root():
    return {"message": "Toto backend is running!"}
