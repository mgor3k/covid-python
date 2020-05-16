import api
import sys
from termcolor import colored

def getStats(country):
	stats = api.fetchStats(country)

	title = country.capitalize() + " COVID-19 stats:"
	deaths = 'Deaths: ' + str(stats.deaths_today) + '/' + colored(stats.deaths, 'red')
	extra = " NO DEATHS TODAY!" if stats.deaths_today == 0 else ""
	recovered = 'Recovered: ' + colored(stats.recovered, 'green')
	cases = 'Cases: ' + str(stats.infected)

	return title + "\n" + deaths + extra + "\n" + recovered + "\n" + cases

def main():
	if len(sys.argv) == 1:
		raise Exception("Come one, at least one country, bro")

	if len(sys.argv) > 2:
		raise Exception("Just one argument please, bro")

	country = sys.argv[1]
	try:
		text = getStats(country)
		print(text)
	except Exception as e:
		print('It\'s not a country, bro' + str(e))


if __name__ == "__main__":
    main()
