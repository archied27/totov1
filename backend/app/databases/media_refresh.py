from app.services.mpv_controller import getMovies, getDetails, getShows, getSeasons, getEpisodes, getSeasonInfo
import sqlite3
from datetime import date
import subprocess
import json
import os

def refresh():
    updateMovies()
    updateShows()

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

    details = {}
    movies = getMovies()
    cur.execute("SELECT file_path FROM files WHERE episode_id IS NULL")
    dbFiles = {row[0] for row in cur.fetchall()}
    diskFiles = {movies[id]['path'] for id in movies}

    if (diskFiles-dbFiles):
        for id in movies:
            if movies[id]['path'] in (diskFiles-dbFiles):
                details = getDetails("movie", id)
                if details != 0:
                    cur.execute("INSERT OR IGNORE INTO media (tmdb_id, type, title, poster_path, date_added)\
                                VALUES(?, ?, ?, ?, ?);", (id, "movie", details["title"], details["poster_path"], date.today()))
                    cur.execute("SELECT id FROM media WHERE (tmdb_id = ?) AND (type=\"movie\")", (id,))
                    medId = cur.fetchone()[0]
                    cur.execute("INSERT OR IGNORE INTO files (media_id, file_path, duration_seconds)\
                                VALUES (?,?,?)", (medId, movies[id]['path'], getMkvDuration(movies[id]['path'])))
                    cur.execute("INSERT OR IGNORE INTO playback (media_id, episode_id, last_watched)\
                                VALUES (?,?,?)", (medId, None, None))

    if (dbFiles-diskFiles):
        con.execute(f"DELETE FROM files WHERE file_path IN ({','.join('?' * len(dbFiles-diskFiles))});", tuple(dbFiles-diskFiles))
    
    con.commit()
    cur.close()
    print("Movies Updated")

def updateShows():
    print("Updating Shows")
    con = sqlite3.connect('app/databases/mediadb.db')
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    details = {}
    shows = getShows()

    cur.execute("SELECT file_path FROM files WHERE episode_id IS NOT NULL")
    dbFiles = {row[0] for row in cur.fetchall()}
    diskFiles = { path for id in shows for season in getSeasons(shows[id]['path']).values() for path in getEpisodes(season).values()}

    if (diskFiles-dbFiles):
        for id in shows:
            details = getDetails("tv", id)
            if details != 0:
                cur.execute("INSERT OR IGNORE INTO media (tmdb_id, type, title, poster_path, date_added)\
                            VALUES(?, ?, ?, ?, ?);", (id, "show", details["title"], details["poster_path"], date.today()))
                cur.execute("SELECT id FROM media WHERE (tmdb_id = ?) AND (type=\"show\")", (id,))

                medId = cur.fetchone()[0]
                seasons = getSeasons(shows[id]['path'])

                for season in seasons:
                    print(f"Season {season}")
                    seasonDetails = getSeasonInfo(id, int(season))
                    
                    cur.execute("INSERT OR IGNORE INTO seasons (media_id, season_number, poster_path) VALUES (?, ?, ?);", \
                        (medId, int(season), seasonDetails["poster_path"]))

                    cur.execute("SELECT id FROM seasons WHERE (media_id = ?) AND (season_number = ?)", (medId, int(season)))
                    seasonId = cur.fetchone()[0]

                    episodes = getEpisodes(seasons[season])

                    for episode in episodes:
                        print(f"Episode {episode}")
                        cur.execute("INSERT OR IGNORE INTO episodes (season_id, episode_number, title, still_path) VALUES (?, ?, ?, ?);", \
                            (seasonId, int(episode), seasonDetails["episodes"][int(episode)]["name"], seasonDetails["episodes"][int(episode)]["still_path"]))

                        cur.execute("SELECT id FROM episodes WHERE (season_id = ?) AND (episode_number = ?)", (seasonId, int(episode)))
                        episodeId = cur.fetchone()[0]

                        cur.execute("INSERT OR IGNORE INTO files (media_id, file_path, duration_seconds, episode_id) VALUES (?, ?, ?, ?);", \
                            (medId, episodes[episode], getMkvDuration(episodes[episode]), episodeId))

                        cur.execute("INSERT OR IGNORE INTO playback (media_id, episode_id) VALUES (?, ?);", \
                            (medId, episodeId))
                            

    if (dbFiles-diskFiles):
        con.execute(f"DELETE FROM files WHERE file_path IN ({','.join('?' * len(dbFiles-diskFiles))});", tuple(dbFiles-diskFiles))

    con.commit()
    cur.close()
    print("Shows Updated")