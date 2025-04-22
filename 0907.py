def compute(n):
    n = str(n)
    return int(n) + int(n*2) + int(n*3) + int(n*4)

# Test for digits 4 to 7
for i in range(4, 8):
    print(f"{i} + {i}{i} + {i}{i}{i} + {i}{i}{i}{i} = {compute(i)}")

