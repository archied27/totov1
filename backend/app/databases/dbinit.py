import sqlite3

con=sqlite3.connect('backend/app/databases/mediadb.db')
con.execute("PRAGMA foreign_keys = ON")
cur = con.cursor()

def createMediaTable(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS media(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        tmdb_id INTEGER NOT NULL,\
        type TEXT NOT NULL CHECK(type IN ('movie','show')),\
        title TEXT NOT NULL,\
        poster_path TEXT,\
        date_added DATETIME,\
        UNIQUE(tmdb_id, type))")

def createSeasonsTable(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS seasons(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        media_id INTEGER NOT NULL,\
        season_number INTEGER NOT NULL,\
        UNIQUE(media_id, season_number),\
        FOREIGN KEY(media_id) REFERENCES media(id) ON DELETE CASCADE)")

def createEpisodesTable(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS episodes(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        season_id INTEGER NOT NULL,\
        episode_number INTEGER NOT NULL,\
        title TEXT,\
        UNIQUE(season_id, episode_number),\
        FOREIGN KEY(season_id) REFERENCES seasons(id) ON DELETE CASCADE)")

def createFilesTable(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS files(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        media_id INTEGER NOT NULL,\
        episode_id INTEGER DEFAULT NULL,\
        file_path TEXT,\
        duration_seconds INTEGER NOT NULL,\
        UNIQUE(file_path)\
        FOREIGN KEY(media_id) REFERENCES media(id) ON DELETE CASCADE,\
        FOREIGN KEY(episode_id) REFERENCES episodes(id) ON DELETE CASCADE)")

def createPlaybackTable(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS playback(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        media_id INTEGER NOT NULL,\
        episode_id INTEGER DEFAULT NULL,\
        progress_seconds INTEGER DEFAULT 0,\
        last_watched DATETIME,\
        completed INTEGER DEFAULT 0,\
        UNIQUE(media_id),\
        FOREIGN KEY(media_id) REFERENCES media(id),\
        FOREIGN KEY(episode_id) REFERENCES episodes(id))")

createMediaTable(cur)
createSeasonsTable(cur)
createEpisodesTable(cur)
createFilesTable(cur)
createPlaybackTable(cur)

con.commit()
con.close()