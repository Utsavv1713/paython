tup = (10, 20, 30)
tup_list = list(tup)
tup_list[1] = 200  # Change 20 to 200
tup = tuple(tup_list)

print("Modified tuple:", tup)
