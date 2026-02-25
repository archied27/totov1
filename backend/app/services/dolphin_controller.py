import socket
import json
import os
import subprocess
import asyncio

GAME_PATHS = ["/media/tssd/games/gamecube"]

def focusHDMI():
    return subprocess.run(["hyprctl", "dispatch", "focusmonitor", "HDMI-A-1"])

def sendKey(key: str):
    if subprocess.run(["hyprctl", "dispatch", "focuswindow", "class:dolphin-emu"]).returncode == 0:
        subprocess.run(["xdotool", "key", key])
        return {"status": "key sent"}

    return {"status": "not open"}

async def close():
    if subprocess.run(["hyprctl", "dispatch", "focuswindow", "class:dolphin-emu"]).returncode == 0:
        subprocess.run(["xdotool", "key", "q"])
        await asyncio.sleep(1)
        subprocess.run(["xdotool", "key", "y"])
        return {"status": "closed"}

    return {"status": "not open"}
    
async def open(path: str):
    focusHDMI()
    await close()
    subprocess.Popen(["dolphin-emu", "-b", "-e", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    return {"game": path}

def getGames():
    games = {}
    for path in GAME_PATHS:
        if os.path.isdir(path):
            for subpath in os.listdir(path):
                if not os.path.isfile(os.path.join(path, subpath)):
                    gamePath = os.path.join(path, subpath, "game.iso")
                    if os.path.isfile(gamePath):
                        games[subpath] =  gamePath
    return games

def fullscreen():
    resp = sendKey("f")
    if resp[status] == "not open":
        return {"status": "not open"}
    return {"status": "fullscreen toggled"}

def pause():
    resp = sendKey("p")
    if resp['status'] == "not open":
        return resp
    return {"status": "pause toggled"}