import requests
import dotenv
import os

dotenv.load_dotenv()
POSTCODE = os.environ.get('POSTCODE')
API_KEY = os.environ.get('WEATHER_API_KEY')
BASE_URL = "http://api.weatherapi.com/v1"

def sendRequest(method: str):
    url = f"{BASE_URL}/{method}"
    params = {
        "key": API_KEY,
        "q": POSTCODE
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def getTodaysWeather():
    return sendRequest("forecast.json")

def getCurrentWeather():
    return sendRequest("current.json")