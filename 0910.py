def ispangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

# Test
print(ispangram("The quick brown fox jumps over the lazy dog"))  # True
print(ispangram("Crazy Fredrick bought many very exquisite opal jewels"))  # True
