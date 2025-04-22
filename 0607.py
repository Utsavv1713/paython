tup = (1, 2, 3, 4)
tup_list = list(tup)
del tup_list[2]  # Remove element at index 2 (which is 3)
tup = tuple(tup_list)

print("Tuple after deletion:", tup)
