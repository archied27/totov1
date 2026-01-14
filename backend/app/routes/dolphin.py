from fastapi import APIRouter
from pydantic import BaseModel
from app.services.dolphin_controller import open, close, getGames

router = APIRouter()

class OpenRequest(BaseModel):
    filePath: str

@router.post("/play")
def openGame(req: OpenRequest):
    return open(req.filePath)

@router.post("/close")
def closeDolph():
    return close()

@router.get("/gameList")
def getGameList():
    return getGames()