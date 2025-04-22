def count_lower_upper(s):
    result = {"uppercase": 0, "lowercase": 0}
    for char in s:
        if char.isupper():
            result["uppercase"] += 1
        elif char.islower():
            result["lowercase"] += 1
    return result

# Test the function with a sample string
sample = "Hello World! Python Is Fun."
counts = count_lower_upper(sample)

# Display results
print("Sample String:", sample)
print("Counts:", counts)
