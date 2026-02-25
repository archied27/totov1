from fastapi import APIRouter
from pydantic import BaseModel
from app.services.spotify_controller import getCurrentTrack

router = APIRouter()

@router.get("/current")
def gCurrentTrack():
    return getCurrentTrack()