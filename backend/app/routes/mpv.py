from fastapi import APIRouter
from pydantic import BaseModel
from app.services.mpv_controller import getCurrTitle, play, closeMpv, fullscreen, playPause, getPause

router = APIRouter()

class PlayRequest(BaseModel):
    filePath:str

@router.get("/title")
def getTitle():
    return getCurrTitle()

@router.post("/play")
def playMPV(req: PlayRequest):
    return play(req.filePath)

@router.post("/close")
def close():
    return closeMpv()

@router.post("/fullscreen")
def fscreen():
    return fullscreen(True)

@router.post("/togglePause")
def tPause():
    return playPause()

@router.post("/getPause")
def gPause():
    return getPause()

