import dotenv
import os
import requests

dotenv.load_dotenv()
spotify_apikey = os.environ.get('SPOTIFY_API_KEY')
BASE_URL = "https://api.spotify.com/v1/"

def getCurrentTrack():
    resp = requests.get(BASE_URL + "me/player/currently-playing", {"Authorization": f"Bearer {spotify_apikey}"})
    print(resp)
    return