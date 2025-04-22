class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

# Test
d1 = Date(22, 4, 2025)
d2 = Date(22, 4, 2025)
d3 = Date(21, 4, 2025)
print("d1 == d2:", d1 == d2)
print("d1 == d3:", d1 == d3)
