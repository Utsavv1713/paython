def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

# Test
arr = create_array(2, 2, 2, 7)
print(arr)
