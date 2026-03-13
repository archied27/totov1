from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import mpv, dolphin, weather, calendar, spotify
from app.databases.media_refresh import refresh
import dotenv
import os

refresh()

dotenv.load_dotenv()

ip_addr = os.getenv("IP_ADDR", "")
extra_origins = [addr.strip() for addr in ip_addr.split(",") if addr.strip()]

app = FastAPI(title="toto backend")

app.include_router(mpv.router, prefix="/mpv", tags=["MPV"])
app.include_router(dolphin.router, prefix="/dolphin", tags=["DOLPHIN"])
app.include_router(weather.router, prefix="/weather", tags=["WEATHER"])
app.include_router(calendar.router, prefix="/calendar", tags=["CALENDAR"])
app.include_router(spotify.router, prefix="/spotify", tags=["SPOTIFY"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ] + extra_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Toto backend is running!"}
