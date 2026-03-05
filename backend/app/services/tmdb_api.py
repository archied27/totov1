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
        newData = {}
        if response.status_code == 200:
            if format=="movie":
                newData["title"] = data["original_title"]
                newData["poster_path"] = data["poster_path"]
            else:
                newData["title"] = data["name"]
                newData["poster_path"] = data["poster_path"]
        else:
            print("INCORRECT ID " + movieID)
            return 0
        return newData

    def getSeasonDetails(self, seriesId, seasonNum):
        url = f"{self.baseUrl}/tv/{seriesId}/season/{seasonNum}"
        params = {
            "api_key" : self.apiKey,
            "language": "en-US"
        }
        response = requests.get(url, params=params)
        data = response.json()
        newData = {}
        if response.status_code == 200:
            newData["episodes"] = {}
            for episode in data["episodes"]:
                newData["episodes"][(episode["episode_number"])] = {"name":episode["name"], "still_path":episode["still_path"]}
            newData["poster_path"] = data["poster_path"]
        else:
            print(f"ERROR FETCHING {seriesId} SEASON {seasonNum}")
            return 0
        return newData