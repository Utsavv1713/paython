class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return Complex(r, i)

    def __truediv__(self, other):
        den = other.real**2 + other.imag**2
        r = (self.real * other.real + self.imag * other.imag) / den
        i = (self.imag * other.real - self.real * other.imag) / den
        return Complex(r, i)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Test
c1 = Complex(4, 5)
c2 = Complex(2, -3)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)
