class Solid:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.data = kwargs

    def surface_area(self):
        if self.shape == "cube":
            return 6 * self.data['side'] ** 2
        elif self.shape == "cylinder":
            r, h = self.data['radius'], self.data['height']
            return 2 * 3.14 * r * (r + h)

    def volume(self):
        if self.shape == "cube":
            return self.data['side'] ** 3
        elif self.shape == "cylinder":
            r, h = self.data['radius'], self.data['height']
            return 3.14 * r**2 * h

# Test
cube = Solid("cube", side=4)
cylinder = Solid("cylinder", radius=3, height=5)
print("Cube Surface Area:", cube.surface_area())
print("Cube Volume:", cube.volume())
print("Cylinder Surface Area:", cylinder.surface_area())
print("Cylinder Volume:", cylinder.volume())
