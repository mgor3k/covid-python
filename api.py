import requests
from stats import Stats

__url = 'https://coronavirus-19-api.herokuapp.com/countries/'

def fetchStats(country):
    request = __url + country
    response = requests.get(request)

    deaths_today = response.json()["todayDeaths"]
    deaths = response.json()["deaths"]
    recovered = response.json()["recovered"]
    infected = response.json()["cases"]

    return Stats(deaths, deaths_today, recovered, infected)
