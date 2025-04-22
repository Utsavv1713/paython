def generate_tuples(end):
    return [(x, x**2, x**3) for x in range(1, end+1)]

# Test
print(generate_tuples(5))
