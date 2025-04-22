tuple_list = [(), (1, 2), (), (3, 4, 5), (), (6,)]

filtered = [t for t in tuple_list if t]
print("List after removing empty tuples:")
print(filtered)
