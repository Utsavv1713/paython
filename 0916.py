def create_list(list1, list2):
    return list(set(list1) & set(list2))

# Test
print(create_list([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
