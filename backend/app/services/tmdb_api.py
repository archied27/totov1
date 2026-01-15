import requests

class MovieFinder:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.baseUrl = 'https://api.themoviedb.org/3'

    def getDetails(self, format, movieID):
        url = f"{self.baseUrl}/{format}/{movieID}"
        params = {
            "api_key" : self.apiKey,
            "language": "en-US"
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data
