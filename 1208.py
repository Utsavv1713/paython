class MyString:
    def __init__(self, s):
        self.s = s

    def __iadd__(self, other):
        self.s += other.s
        return self

    def toLower(self):
        return self.s.lower()

    def toUpper(self):
        return self.s.upper()

    def __str__(self):
        return self.s

# Test
s1 = MyString("Hello")
s2 = MyString("World")
s1 += s2
print("Concatenated:", s1)
print("To Lower:", s1.toLower())
print("To Upper:", s1.toUpper())
