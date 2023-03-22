import requests as re
from headers import headers
from selectorlib import Extractor


class Temperature:
    base_url = 'https://www.timeanddate.com/weather/'
    yaml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.city = city.replace(' ', '-')
        self.country = country.replace(' ', '-')

    def _build_url(self):
        url = self.base_url + self.country + '/' + self.city
        return url

    def _scrape(self):
        url = self._build_url()
        webpage = re.get(url, headers)
        content = webpage.text
        extractor = Extractor.from_yaml_file(self.yaml_path)
        raw_result = extractor.extract(content)
        return raw_result

    def get(self):
        temp = self._scrape()['temp'][:2]
        return float(temp)


class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - (5 / 9 * self.temperature - 32) * 10
        return round(result, 2)


if __name__ == '__main__':
    temperature = Temperature('usa', 'miami')
    calorie = Calorie(80, 183, 26, temperature.get())
    print(calorie.calculate())
