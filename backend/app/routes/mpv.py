from fastapi import APIRouter
from pydantic import BaseModel
from app.services.mpv_controller import getCurrTitle, play, closeMpv, fullscreen, playPause, getPause, getMovies, getShows, getEpisodes, getSeasons, getMoviesDetails, getDetails, getShowsDetails

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

@router.get("/movieList")
def gMovies():
    return getMovies()

@router.get("/showList")
def gShows():
    return getShows()

@router.get("/seasonsList")
def gSeasons(path: str):
    return getSeasons(path)

@router.get("/episodesList")
def gEpisodes(path: str):
    return getEpisodes(path)

@router.get("/movieListPlus")
def gMoviesPlus():
    return getMoviesDetails()

@router.get("/movieDetails")
def getMovieDetails(id: int):
    return getDetails("movie", id)

@router.get("/showDetails")
def getShowDetails(id: int):
    return getDetails("tv", id)

@router.get("/showListPlus")
def gShowsPlus():
    return getShowsDetails()