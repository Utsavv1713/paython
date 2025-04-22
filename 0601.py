data = [("John",), ("Mike",), "Alice", "Emma", ("Ryan",), "Sophie"]

boys = sum(1 for x in data if isinstance(x, tuple))
girls = sum(1 for x in data if not isinstance(x, tuple))

print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")
