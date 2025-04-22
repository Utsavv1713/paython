def sanitize_list(lst):
    if not lst:
        return []
    return [0 if lst[0] < 0 else lst[0]] + sanitize_list(lst[1:])

# Main
values = [5, -3, 8, -1, 4]
print("Sanitized list:", sanitize_list(values))
