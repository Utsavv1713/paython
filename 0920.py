def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + reverse_list(lst[:-1])

# Main
lst = [1, 2, 3, 4, 5]
print("Original List:", lst)
print("Reversed List:", reverse_list(lst))
