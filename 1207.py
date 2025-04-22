class Weather:
    def __init__(self, parameters):
        self.params = parameters

    def __contains__(self, item):
        return item in self.params

# Test
w = Weather(["Temperature", "Humidity", "Wind"])
print("Humidity" in w)   # True
print("Pressure" in w)   # False
