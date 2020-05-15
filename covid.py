import requests
import sys
from termcolor import colored

if len(sys.argv) == 1:
	raise Exception("Come one, at least one country, bro")

if len(sys.argv) > 2:
	raise Exception("Just one argument please, bro")

country = sys.argv[1]

def getStats(country):
	url = 'https://coronavirus-19-api.herokuapp.com/countries/' + country
	r = requests.get(url)

	todayJson = r.json()["todayDeaths"]
	overallJson = r.json()["deaths"]
	recoveredJson = r.json()["recovered"]
	casesJson = r.json()["cases"]

	title = country.capitalize() + " COVID-19 stats:"
	deaths = 'Deaths: ' + str(todayJson) + '/' + colored(overallJson, 'red')
	extra = " NO DEATHS TODAY!" if todayJson == 0 else ""
	recovered = 'Recovered: ' + colored(recoveredJson, 'green')
	cases = 'Cases: ' + str(casesJson)

	return title + "\n" + deaths + extra + "\n" + recovered + "\n" + cases
try:
	text = getStats(country)
	print(text)
except Exception as e:
	print('It\'s not a country, bro')
