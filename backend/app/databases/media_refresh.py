from app.services.mpv_controller import getMovies, getDetails
import sqlite3
from datetime import date
import subprocess
import json
import os

def refresh():
    updateMovies()

def getMkvDuration(filepath: str):
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "json",
            filepath
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    data = json.loads(result.stdout)
    duration = float(data["format"]["duration"])
    return int(duration)

def updateMovies():
    print("Updating Movies")
    con = sqlite3.connect('app/databases/mediadb.db')
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    movies = getMovies()
    if movies != {}:
        for id in movies:
            details = getDetails("movie", id)
            if details != 0:
                cur.execute("INSERT OR IGNORE INTO media (tmdb_id, type, title, poster_path, date_added)\
                            VALUES(?, ?, ?, ?, ?);", (id, "movie", details["title"], details["poster_path"], date.today()))
                cur.execute("SELECT id FROM media WHERE tmdb_id = ?", (id,))
                medId = cur.fetchone()[0]
                cur.execute("INSERT OR IGNORE INTO files (media_id, file_path, duration_seconds)\
                            VALUES (?,?,?)", (medId, movies[id]['path'], getMkvDuration(movies[id]['path'])))
                cur.execute("INSERT OR IGNORE INTO playback (media_id, episode_id, last_watched)\
                            VALUES (?,?,?)", (medId, None, None))
    
    con.commit()
    cur.close()
    print("Movies Updated")
    return details