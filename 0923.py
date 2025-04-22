def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

def average_list(lst):
    if not lst:
        return 0
    return sum_list(lst) / len(lst)

# Main
nums = [10, 20, 30, 40, 50]
print(f"Average: {average_list(nums)}")
