import requests
import json


countries_fact = requests.get("https://restcountries.com/v3.1/name/netherlands")
print(countries_fact)
print(countries_fact.json()[1])