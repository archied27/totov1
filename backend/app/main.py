from fastapi import FastAPI
from app.routes import mpv, dolphin, weather

app = FastAPI(title="toto backend")

app.include_router(mpv.router, prefix="/mpv", tags=["MPV"])
app.include_router(dolphin.router, prefix="/dolphin", tags=["DOLPHIN"])
app.include_router(weather.router, prefix="/weather", tags=["WEATHER"])

@app.get("/")
def root():
    return {"message": "Toto backend is running!"}
