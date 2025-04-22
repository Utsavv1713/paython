def sum_avg(*marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

# Test
total, avg = sum_avg(85, 90, 78, 92, 88)
print(f"Total: {total}, Average: {avg}")
