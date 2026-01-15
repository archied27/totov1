from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import mpv, dolphin, weather, calendar
import dotenv
import os

dotenv.load_dotenv()
IP_ADDR = os.environ.get('IP_ADDR')

app = FastAPI(title="toto backend")

app.include_router(mpv.router, prefix="/mpv", tags=["MPV"])
app.include_router(dolphin.router, prefix="/dolphin", tags=["DOLPHIN"])
app.include_router(weather.router, prefix="/weather", tags=["WEATHER"])
app.include_router(calendar.router, prefix="/calendar", tags=["CALENDAR"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        IP_ADDR
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Toto backend is running!"}
