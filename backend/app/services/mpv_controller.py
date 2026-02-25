import socket
import json
import os
import subprocess
import re
import dotenv
import sqlite3
from app.services.tmdb_api import MovieFinder

MPV_SOCKET = "/tmp/mpvsocket"
MOVIES_PATHS = ["/media/tssd/movies"]
SHOWS_PATHS = ["/media/tssd/shows"]
dotenv.load_dotenv()
tmdbApiKey = os.environ.get('TMDB_API_KEY')
tmdbFinder = MovieFinder(tmdbApiKey)

def focusHDMI():
    return subprocess.run(["hyprctl", "dispatch", "focusmonitor", "HDMI-A-1"])

def removeID(filename: str):
    match = re.match(r"^\((\d+)\)(.+)$", filename)
    if not match:
        return {'id': None, 'newfile': filename}
    return {'id': match.group(1), 'newfile': match.group(2)}

def testMpv():
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        client.connect(MPV_SOCKET)
        return True
    except (FileNotFoundError, ConnectionRefusedError, socket.error):
        return False

def closeMpv():
    if testMpv():
       send_mpv_command("quit")
    else:
        subprocess.run(["pkill", "-f", "mpv"], check=False)
    return {"status": "closed"}
    
def send_mpv_command(command: str, args=None):
    payload = {"command": [command]}
    if args:
        payload["command"].extend(args)
    payload = json.dumps(payload).encode("utf-8") + b"\n"
    
    if not testMpv():
        return -1

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(MPV_SOCKET)
        client.sendall(payload)
        response = client.recv(4096)
        client.close()
        return json.loads(response.decode("utf-8"))

def getCurrTitle():
    resp = getPathBeingPlayed()
    if resp["path"] == None:
        return {"title": None, "error": "mpv not open in correct mode"}
    else:
        c = -1
        fName = resp["path"]
        while(fName[c] != '/'):
            c-=1
        fName = fName[c+1:]
        splitFile = removeID(fName)
        title = splitFile['newfile'].replace("-", " ")
        return {"title": title[:-4], "error": None}


def play(path: str):
    closeMpv()
    focusHDMI()
    subprocess.Popen(["mpv", path, "-fs", f"--input-ipc-server={MPV_SOCKET}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    return{"status": "started", "file": path}

def fullscreen(val: bool):
    if send_mpv_command("set_property", ["fullscreen", val]) == -1:
        return {"status": "mpv not open in correct mode"}
    else:
        return {"status": "fullscreen toggled"}

def playPause():
    status = getPause()
    if status == -1:
        return {"status": "mpv not open in correct mode"}
    else:
        send_mpv_command("set_property", ["pause", not status.get("pause")])
        return {"status": not status.get("pause")}

def getPause():
    response = send_mpv_command("get_property", ["pause"])
    
    if response == -1:
        return {"pause": None, "status": "mpv not open in correct mode"}
    else:
        return {"pause": response.get('data')}

def getMovies():
    movies = {}
    for path in MOVIES_PATHS:
        if os.path.isdir(path):
            for f in os.listdir(path):
                file = os.path.join(path, f)
                if os.path.isfile(file):
                    splitFile = removeID(f)
                    title = splitFile['newfile'].replace("-", " ")
                    movie = {"title": title[:-4], "path":file}
                    movies[splitFile['id']] = movie
    return movies

def getShows():
    shows = {}
    for path in SHOWS_PATHS:
        if os.path.isdir(path):
            for subpath in os.listdir(path):
                if not os.path.isfile(os.path.join(path, subpath)):
                    splitFile = removeID(subpath)
                    title = splitFile['newfile'].replace("-", " ")
                    show = {"title": title, "path":os.path.join(path,subpath)}
                    shows[splitFile['id']] = show
    return shows

def getSeasons(showPath: str):
    seasons = {}
    for path in os.listdir(showPath):
        if not os.path.isfile(os.path.join(showPath, path)):
            if path[0]=='s':
                season = f"Season {path[1:]}"
                seasons[season] = os.path.join(showPath, path)
    return seasons

def getEpisodes(seasonPath: str):
    episodes = {}
    for path in os.listdir(seasonPath):
        if os.path.isfile(os.path.join(seasonPath, path)):
            if path[0]=='e':
                episode = f"Episode {path[1:-4]}"
                episodes[episode] = os.path.join(seasonPath, path)
    return episodes

def getPathBeingPlayed():
    resp = send_mpv_command("get_property", ["path"])
    if resp == -1 or resp.get("error") != "success":
        return {"path": None}
    return {"path": resp.get("data")}

def getDetails(format: string, id: int):
    # format: tv or movie
    return tmdbFinder.getDetails(format, id)

def getMoviesDetails():
    details = {}
    print('he;lo')
    with sqlite3.connect("app/databases/mediadb.db") as conn:
        cur = conn.cursor()
        cur.execute('SELECT media.tmdb_id, media.title, media.poster_path, files.file_path \
            FROM media INNER JOIN files ON (files.media_id=media.id) WHERE type="movie"')
        rows=cur.fetchall()
        for row in rows:
            details[row[0]] = {'title': row[1], 'poster_path': row[2], 'file_path': row[3]}
    return details



    """
    movies = getMovies()
    details = {}
    if movies != {}:
        for id in movies:
            details[id] = getDetails("movie", id)
            details[id]["file_path"] = movies[id]["path"]
    return details
    """

def getShowsDetails():
    shows = getShows()
    details = {}
    if shows != {}:
        for id in shows:
            details[id] = getDetails("tv", id)
            details[id]["file_path"] = shows[id]["path"]
    return details

def getCurrentDetails():
    path = getPathBeingPlayed()['path']
    if path==None:
        return None
    if "shows" in path:
        format = "tv"
    else:
        format = "movie"
    c = -1
    while(path[c] != '/'):
            c-=1
    path = path[c+1:]
    splitFile = removeID(path)
    return getDetails(format, splitFile['id'])