def number_to_word(n):
    words = [
        "zero", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    
    if 0 <= n <= 19:
        return words[n]
    else:
        return "Number out of range (0–19)"

# Test
for i in range(20):
    print(f"{i} → {number_to_word(i)}")
