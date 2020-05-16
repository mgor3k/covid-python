from termcolor import colored

class Formatter:

    @staticmethod
    def stringFrom(country, stats):
        topBorder = "---"
        leftBorder = "| "
        bottomBorder = "--------"

        title = country.capitalize() + " COVID-19 stats"
        deaths = leftBorder + 'Deaths: ' + str(stats.deaths_today) + '/' + colored(stats.deaths, 'red')
        recovered = leftBorder + 'Recovered: ' + colored(stats.recovered, 'green')
        cases = leftBorder + 'All cases: ' + str(stats.infected)

        return topBorder + " " + title + "\n" + deaths + "\n" + recovered + "\n" + cases + "\n" + bottomBorder
