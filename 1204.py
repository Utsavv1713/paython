class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        self.data = kwargs

    def area(self):
        if self.shape_type == "circle":
            return 3.14 * self.data['radius'] ** 2
        elif self.shape_type == "square":
            return self.data['side'] ** 2

    def perimeter(self):
        if self.shape_type == "circle":
            return 2 * 3.14 * self.data['radius']
        elif self.shape_type == "square":
            return 4 * self.data['side']

# Test
circle = Shape("circle", radius=7)
square = Shape("square", side=5)
print("Circle Area:", circle.area(), "Perimeter:", circle.perimeter())
print("Square Area:", square.area(), "Perimeter:", square.perimeter())
