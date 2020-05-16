import api
import sys
from formatter import Formatter

def getStats(country):
	stats = api.fetchStats(country)
	return Formatter.stringFrom(country, stats)

def main():
	if len(sys.argv) == 1:
		raise Exception("Come one, at least one country, bro")

	if len(sys.argv) > 2:
		raise Exception("Just one argument please, bro")

	country = sys.argv[1]
	try:
		stats = api.fetchStats(country)
		formatted_text = Formatter.stringFrom(country, stats)
		print(formatted_text)
		
	except Exception as e:
		print('It\'s not a country, bro' + str(e))


if __name__ == "__main__":
    main()
