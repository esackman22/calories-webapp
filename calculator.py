class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        pass

class Temperature:

    def __init__(self, country, city):
        self.city = city
        self.country = country

    def get(self):
        pass