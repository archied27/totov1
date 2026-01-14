import socket
import json
import os
import subprocess

GAME_PATHS = ["/media/tssd/games/gamecube"]

def close():
    return subprocess.run(["pkill", "-f", "dolphin-emu"]).returncode
    
def open(path: str):
    close()
    subprocess.Popen(["dolphin-emu", "-b", "-e", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    return {"game": path}

def getGames():
    games = {}
    for path in GAME_PATHS:
        for subpath in os.listdir(path):
            if not os.path.isfile(os.path.join(path, subpath)):
                gamePath = os.path.join(path, subpath, "game.iso")
                if os.path.isfile(gamePath):
                    games[subpath] =  gamePath
    return games