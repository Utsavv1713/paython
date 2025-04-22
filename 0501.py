import random

# Step 1: Create a list of 5 random odd integers
odd_integers = [random.choice(range(1, 100, 2)) for _ in range(5)]
print("Step 1: List of 5 random odd integers:")
print(odd_integers)

# Step 2: Create a list of 4 random even integers
even_integers = [random.choice(range(2, 100, 2)) for _ in range(4)]
print("\nStep 2: List of 4 random even integers:")
print(even_integers)

# Step 3: Replace the third element in odd list with the even list
odd_integers[2] = even_integers
print("\nStep 3: Replacing 3rd element in odd list with even list:")
print(odd_integers)

# Step 4: Flatten the nested list
flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print("\nStep 4: Flattened list:")
print(flattened_list)

# Step 5: Sort the flattened list
flattened_list.sort()
print("\nStep 5: Sorted flattened list:")
print(flattened_list)
