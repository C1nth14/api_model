# This class is created so it can hold the data we are interested in


class SingleNameModel:
    def __init__(self, single_name):
        self.status = single_name['status']
        self.result = single_name['name']
        self.official = self.result['official']
        self.currency = self.result['currencies']
        self.capital = self.result['capital']
        self.subregion = self.result['subregion']
        self.language = self.result['languages']
