# This class is created so it can hold the data we are interested in


class SingleNameModel:
    def __init__(self, single_name):
        self.result = single_name[0]
        self.official = self.result['name']
        self.currency = self.result['currencies']
        self.capital = self.result['capital']
        self.subregion = self.result['subregion']
        self.language = self.result['languages']
        self.landlocked = self.result['landlocked']
        self.car = self.result['car']
        self.continent = self.result['continents']

