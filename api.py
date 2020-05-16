import requests

__url = 'https://coronavirus-19-api.herokuapp.com/countries/'

class Stats:
    def __init__(self, deaths, deaths_today, recovered, infected):
        self.deaths = deaths
        self.deaths_today = deaths_today
        self.recovered = recovered
        self.infected = infected

def fetchStats(country):
    request = __url + country
    response = requests.get(request)

    deaths_today = response.json()["todayDeaths"]
    deaths = response.json()["deaths"]
    recovered = response.json()["recovered"]
    infected = response.json()["cases"]

    return Stats(deaths, deaths_today, recovered, infected)
