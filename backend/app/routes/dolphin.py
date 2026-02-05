from fastapi import APIRouter
from pydantic import BaseModel
from app.services.dolphin_controller import open, close, getGames, fullscreen, pause

router = APIRouter()

class OpenRequest(BaseModel):
    filePath: str

@router.post("/play")
async def openGame(req: OpenRequest):
    return await open(req.filePath)

@router.post("/close")
async def closeDolph():
    result = await close()
    return result

@router.get("/gameList")
def getGameList():
    return getGames()

@router.post("/fullscreen")
def fScreen():
    return fullscreen()

@router.post("/playPause")
def pPause():
    return pause()