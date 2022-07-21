from single_name_model import SingleNameModel
import requests


class SingleName:
    def __init__(self, s_name):
        self.url = "https://restcountries.com/v3.1/name/" + s_name
        self.request = requests.get(self.url)
        self.resp_json = self.request.json()

    def response_data(self):
        return SingleNameModel(self.resp_json)
