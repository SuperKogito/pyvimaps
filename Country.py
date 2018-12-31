import json
import pycountry

class Country():
    def __init__(self, alpha_two_code):
        with open("data.json", "r") as f:
            self.data = json.load(f)

        self.name    = self.data[alpha_two_code]['name']
        self.alpha3  = self.data[alpha_two_code]['alpha3']
        self.numeric = self.data[alpha_two_code]['numeric']
        self.lower_lattitude_bound = self.data[alpha_two_code]['lower_lattitude_bound']
        self.lower_longitude_bound = self.data[alpha_two_code]['lower_longitude_bound']
        self.upper_lattitude_bound = self.data[alpha_two_code]['upper_lattitude_bound']
        self.upper_longitude_bound = self.data[alpha_two_code]['upper_longitude_bound']
        self.states = [i.name for i in pycountry.subdivisions.get(country_code=alpha_two_code)]
