from fastapi import APIRouter
from pydantic import BaseModel
from app.services.weather_controller import getCurrentWeather, getTodaysWeather

router = APIRouter()

class OpenRequest(BaseModel):
    filePath: str

@router.get("/current")
def getCurrent():
    return getCurrentWeather()

@router.get("/today")
def getToday():
    return getTodaysWeather()